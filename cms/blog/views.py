from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm,UpdateForm
from django.urls import reverse_lazy
# Create your views here.

# def home(request):
#     context = {}
#     return render(request,'home.html',context)

class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date']

class Article(DetailView):
    model = Post
    template_name = 'article.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePost(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

