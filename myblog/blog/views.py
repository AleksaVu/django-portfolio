from django.shortcuts import render
from .models import Post

def post_listing(request):
    posts = Post.objects.all()
    
    return render(request, 'blog/post_listing.html', {'posts': posts})

