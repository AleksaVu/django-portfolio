from django.shortcuts import render
from .models import Project


def project_listing(request):
    """ View all projects"""
    projects = Project.objects.all()
    return render(request, 'projects/project_listing.html', {'projects': projects})


def project_detail(request, project_id):
    """ A view of project detail"""
    project = Project.objects.get(pk=project_id)
    return render(request, 'projects/project_detail.html', {'project': project})