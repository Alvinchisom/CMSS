from django.urls import path
from .views import UserRegister,UserProfile,PasswordsView,password_success,EditProfile
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/',UserRegister.as_view(),name='register'),
    path('user_profile/',UserProfile.as_view(),name='user_profile'),
    path('success_password/',password_success,name='success_password'),
    path('password/',PasswordsView.as_view(template_name='registration/change_password.html'),name='password_change'),
    path('edit_profile/<int:pk>/',EditProfile.as_view(),name='edit_profile'),
]