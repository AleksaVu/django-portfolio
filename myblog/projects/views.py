from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from .forms import AddProjectForm
from .models import Member, Project


def project_listing(request):
    """ View all projects"""
    projects = Project.objects.all()
    return render(request, 'projects/project_listing.html', {'projects': projects})


def project_detail(request, project_id):
    """ A view of project detail"""
    project = Project.objects.get(pk=project_id)        
    return render(request, 'projects/project_detail.html', {'project': project})


def project_search(request):
    """ A view of searched projects"""
    queried_project = request.GET.get('q')
    # project = Project.objects.get(name__icontains=queried_project)    
    project = None
    try:
        project = Project.objects.get(name__iexact=queried_project)        
        queried_project_exists = True
    except:
        queried_project_exists = False
    return render(request, 'projects/project_searched.html', {'project': project , 'results': queried_project_exists})

@login_required
def add_project(request):
    form = AddProjectForm(request.POST or None)        
    if form.is_valid():
        # new_project = form.save(commit=False)        
        # new_project = form.save()
        form.save()
    return render(request, 'projects/add_project.html', {'form': form})