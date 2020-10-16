from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from .models import Post, Comment


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogs/home.html', context)


class PostListView(ListView):
    """docstring for PostListView."""
    model = Post
    template_name = 'blogs/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    """docstring for PostListView."""
    model = Post
    template_name = 'blogs/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def qet_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return super().objects.filter(author=user)


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
# this is actually complicated - need further explanation

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
# this is actually complicated - need further explanation

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blogs/about.html')


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(post)
    print(Post.pk)
    print(post.pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid() and request.user.is_authenticated():
            comment = c_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
        elif c_form.is_valid():
            comment = c_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        c_form = CommentForm(request.POST)

    context = {
        'c_form': c_form
    }

    return render(request, 'blogs/add_comment_to_post.html', context)


class CommentUpdateView(UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
