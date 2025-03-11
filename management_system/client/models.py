from django.db import models
from project.models import Project

# Create your models here.
class Client(models.Model):
    client_id = models.CharField(max_length=100,primary_key=True)
    client_name = models.CharField(max_length=100)
    client_image = models.ImageField(upload_to="clients")
    client_email= models.EmailField()
    client_contact_number = models.PositiveBigIntegerField()
    client_address= models.TextField(default="Please enter the address.")
    client_projects= models.ForeignKey(Project,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.client_name