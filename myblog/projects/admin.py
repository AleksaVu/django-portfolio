from django.contrib import admin
from .models import Project


#admin.site.register(Project)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'completed')
    list_filter = ('completed',)

admin.site.register(Project, ProjectAdmin)