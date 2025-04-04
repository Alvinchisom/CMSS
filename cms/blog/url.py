from django.urls import path
from .views import *


urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('article/<int:pk>/',Article.as_view(),name='article_page'),
    path('add_post/',AddPost.as_view(),name='add_post'),
    path('update_post/<int:pk>/',UpdatePost.as_view(),name='update_post'),
]