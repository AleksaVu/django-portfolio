from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_listing, name='post-listing'),    
    path('blog-post/<int:post_id>/', views.blog_post, name='blog-post'),  
    path('blog-post/search/', views.post_search, name='post-search'),  
]