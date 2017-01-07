from django.db import models

# Create your models here.
from django.utils import timezone


class Book (models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
