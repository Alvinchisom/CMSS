from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        # fields = ['title','body']
        fields = ['title','category','body']

class UpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','category','body']
        # fields = '__all__'