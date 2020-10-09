from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


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
    # paginate_by = 5


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'blogs/about.html')
