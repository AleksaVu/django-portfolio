from django.urls import path

from . import views

urlpatterns = [
    path('projects/', views.project_listing, name='project-listing'),
    #path('projects/<int:project_id>/', views.project_detail, name='project-detail'),
    # path('projects/search/', views.project_search, name='project-search'),
]
