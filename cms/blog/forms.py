from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        # fields = ['title','body']
        fields = '__all__'

class UpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']
        # fields = '__all__'