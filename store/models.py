from django.db import models

# Create your models here.
from django.utils import timezone


class Book (models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=8)
    stock = models.IntegerField(default=0)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)


class Buty (models.Model):
    brand = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    size = models.DecimalField(decimal_places=1,max_digits=3, default=0)
    price = models.DecimalField(decimal_places=2, max_digits=8, default=0)
