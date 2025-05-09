from django.urls import path
from .views import *


urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('article/<int:pk>/',Article.as_view(),name='article_page'),
    path('add_post/',AddPost.as_view(),name='add_post'),
    path('update_post/<int:pk>/',UpdatePost.as_view(),name='update_post'),
    path('delete_post/<int:pk>/',DeletePost.as_view(),name='delete_post'),
    path('add_category/',AddCategory.as_view(),name='add_category'),
    path('like_Post/<int:pk>/',likePost,name='like_Post'),
    path('add_comment/<int:pk>/',AddComment.as_view(),name='add_comment'),
    path('search_page/',search,name='search_page'),
]