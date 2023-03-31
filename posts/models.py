from django.db import models

from django.contrib.auth import get_user_model

from core.models import CreatedModel

User = get_user_model()


class Post(CreatedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title