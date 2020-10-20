from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=120, default='misc')
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey('blogs.Post', on_delete=models.CASCADE, related_name='comments')
    comment_title = models.CharField(max_length=100, default='Title')
    words = models.TextField()
    signature = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.words


class Category(models.Model):
    post_cat = models.CharField(max_length=120, default='misc')

    def __str__(self):
        return self.post_cat

    def get_absolute_url(self):
        return reverse('blogs-home')
