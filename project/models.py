from django.db import models
from user.models import CustomUser

# Create your models here.
class Project(models.Model):
    project_name= models.CharField(max_length=100)
    project_logo = models.ImageField(upload_to="projects")
    project_description = models.TextField(default="Enter the project description.")
    project_duration= models.CharField(max_length=100)
    assigned_to = models.ManyToManyField(CustomUser,related_name="project_list")
     
    def __str__(self):
        return self.project_name

# class Assigned(models.Model):
#     assigned_to = models.CharField(max_length=100,null=False)
#     user = models.ManyToManyField(User)