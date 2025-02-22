from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
#from .form import CustomUserCreationForm
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from .models import Client

# Create your views here.
class ClientListView(ListView):
    model = Client
    template_name = "clients/client_list.html"

class ClientDetailView(DetailView):
    model = Client
    template_name = "clients/client_detail.html"

class ClientCreateView(CreateView):
    model = Client
    fields="__all__"
    success_url = "/display-clients"
    template_name = "clients/client_form.html"

class ClientUpdateView(UpdateView):
    model = Client
    fields="__all__"
    success_url = "/display-clients"
    template_name = "clients/client_form.html"

class ClientDeleteView(DeleteView):
    model = Client
    success_url = "/display-clients"
    template_name = "clients/client_confirm_delete.html"

