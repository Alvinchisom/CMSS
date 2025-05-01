from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category,Comment
from .forms import PostForm,UpdateForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
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

    def get_context_data(self,*args,**kwargs):
        context = super(Article,self).get_context_data(*args,**kwargs)
        some = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = some.total_likes()
        total_comments = some.comments.count()

        liked = False
        if some.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        context["total_comments"] = total_comments
        return context

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePost(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategory(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

def likePost(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('likes_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_page',args=[str(pk)]))

class AddComment(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = ['name','body']

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article_page',kwargs= {'pk': self.kwargs['pk']})