from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import UserProfileView
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