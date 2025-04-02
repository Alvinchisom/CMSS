from django.urls import path
from .views import *


urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('article/<int:pk>/',Article.as_view(),name='article_page'),
]