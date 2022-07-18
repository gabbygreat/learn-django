from django.db import models
from datetime import datetime

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.title
