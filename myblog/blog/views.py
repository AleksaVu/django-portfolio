from django.shortcuts import render
from .models import Post

def post_listing(request):
    posts = Post.objects.all()    
    return render(request, 'blog/post_listing.html', {'posts': posts})

def blog_post(request, post_id):
    post = Post.objects.get(id=post_id)    
    return render(request, 'blog/blog_post.html', {'post': post})

def post_search(request):
    """ A view of searched post"""
    queried_post = request.GET.get('q')    
    post = None
    try:
        post = Post.objects.get(title__iexact=queried_post)        
        queried_post_exists = True
    except:
        queried_post_exists = False
    return render(request, 'blog/post_searched.html', {'post': post , 'results': queried_post_exists})