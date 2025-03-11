from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]  

    gender = models.CharField(null=True,blank=False,max_length=100,choices=GENDER_CHOICES)
    phone_number = models.PositiveBigIntegerField(default=0) 

    def __str__(self):
        return self.username 