from django.shortcuts import render
from projects.models import Project


def homepage(request):
    projects = Project.objects.all().order_by('id')[:3]
    return render(request, 'cms/homepage.html', {'projects': projects})

