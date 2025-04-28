from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import UserProfileView
from django.contrib.auth.views import PasswordChangeView
from blog.models import Profile
# Create your views here.

class UserRegister(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserProfile(generic.UpdateView):
    model = User
    form_class = UserProfileView
    template_name = 'registration/user_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('success_password')

def password_success(request):
    context = {}
    return render(request,'registration/success_password.html',context)

class EditProfile(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['bio','profile_pic','instagram_url','facebook_url','linkedin_url']
    success_url = reverse_lazy('home')
