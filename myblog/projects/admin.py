from django.contrib import admin
from .models import Member, Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'completed')
    list_filter = ('completed',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Member)