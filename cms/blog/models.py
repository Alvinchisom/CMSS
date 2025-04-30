from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
from django.templatetags.static import static
from django.db.models.signals import post_save
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank=True)
    bio = RichTextField(null=True,blank=True)
    instagram_url = models.CharField(max_length=200,null=True,blank=True)
    facebook_url = models.CharField(max_length=200, null=True, blank=True)
    linkedin_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def profile_url(self):
        if self.profile_pic:
            return self.profile_pic.url
        else:
            return static('images/pexels-camcasey-1687093.jpg')

    def create_profile(sender,instance,created,**kwargs):
        if created:
            user_profile = Profile(user=instance)
            user_profile.save()
    post_save.connect(create_profile,sender=User)

class Post(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    body = RichTextField(null=True,blank=True)
    # body = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name='post_likes')

    def __str__(self):
        return str(self.author) + ' = ' + self.title

    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self):
        return self.likes.count()

    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return static('images/pexels-camcasey-1687093.jpg')

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.post.title}"