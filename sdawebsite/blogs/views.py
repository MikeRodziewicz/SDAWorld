from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Mike',
        'title': 'First post',
        'content': 'bla bla first',
        'date_posted': 'October 2020'
    },
    {
        'author': 'Ela',
        'title': 'Second post',
        'content': 'bla bla second',
        'date_posted': 'September 2020'
    }


]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogs/home.html', context)


def about(request):
    return render(request, 'blogs/about.html')
