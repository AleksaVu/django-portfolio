from django.shortcuts import render
from projects.models import Project
from blog.models import Post


def homepage(request):
    projects = Project.objects.all().order_by('id')[:4]
    posts = Post.objects.all().order_by('id')[:3]
    return render(request, 'cms/homepage.html', {'projects': projects, 'posts':posts})


def aboutme(request):
    return render(request, 'cms/aboutme.html')
