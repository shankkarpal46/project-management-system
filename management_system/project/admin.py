from django.contrib import admin
from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','project_name','project_logo','project_description','project_duration']

admin.site.register(Project,ProjectAdmin)

