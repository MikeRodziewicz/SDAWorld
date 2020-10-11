from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey('blogs.Post', on_delete=models.CASCADE, related_name='comments')
    words = models.TextField()
    signature = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment
