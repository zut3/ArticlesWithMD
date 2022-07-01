from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=128, null=False)
    text = models.TextField(verbose_name="Text of Article")
    created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
