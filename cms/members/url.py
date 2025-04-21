from django.urls import path
from .views import UserRegister,UserProfile


urlpatterns = [
    path('register/',UserRegister.as_view(),name='register'),
    path('user_profile/',UserProfile.as_view(),name='user_profile'),
]