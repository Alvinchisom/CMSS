from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.

# def home(request):
#     context = {}
#     return render(request,'home.html',context)

class Home(ListView):
    model = Post
    template_name = 'home.html'

class Article(DetailView):
    model = Post
    template_name = 'article.html'
