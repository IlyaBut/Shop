from django.db import models
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')


