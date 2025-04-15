from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + ' = ' + self.title

    def get_absolute_url(self):
        return reverse('home')

