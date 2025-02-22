from django.contrib import admin
from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_id','client_name','client_image','client_email','client_contact_number','client_address','client_projects']

admin.site.register(Client,ClientAdmin)