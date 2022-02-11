from django.shortcuts import render
from projects.models import Project
from blog.models import Post
from django.contrib.auth.models import User


def homepage(request):
    projects = Project.objects.all().order_by('-id')[:4]
    posts = Post.objects.all().order_by('-id')[:3]
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'cms/homepage.html', {'projects': projects, 'posts':posts, 'username': username})


def aboutme(request):
    return render(request, 'cms/aboutme.html')
