from django.shortcuts import render
from .models import Project

# Create your views here.

def project_listing(request):
    """ View all projects"""
    projects = Project.objects.all()
    return render(request, 'projects/project_listing.html', {'projects': projects})
