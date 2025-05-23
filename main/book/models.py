from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank= True)

    def __str__(self):
        return self.title


