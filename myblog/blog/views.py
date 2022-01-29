from django.shortcuts import render
from .forms import CommentForm
from .models import Post, Comment


def post_listing(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_listing.html', {'posts': posts})


def blog_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = CommentForm(request.POST or None)
    #comments = post.comments.all()
    new_comment = None
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.post = post
        new_comment = form.save()        
    return render(request, 'blog/blog_post.html', {'post': post, 'form': form, 'new_comment':new_comment})


def post_search(request):
    """ A view of searched post"""
    queried_post = request.GET.get('q')
    post = None
    try:
        post = Post.objects.get(title__iexact=queried_post)
        queried_post_exists = True
    except:
        queried_post_exists = False
    return render(request, 'blog/post_searched.html', {'post': post, 'results': queried_post_exists})


