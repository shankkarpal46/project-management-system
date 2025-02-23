from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
#from .form import CustomUserCreationForm
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from .models import Project
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
def home(request):
    return render(request,"index.html",{})

class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"

class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"

@method_decorator(staff_member_required,name="dispatch")
class ProjectCreateView(CreateView):
    model = Project
    fields="__all__"
    success_url = "/management/project-list"
    template_name = "projects/project_form.html"

@method_decorator(staff_member_required,name="dispatch")
class ProjectUpdateView(UpdateView):
    model = Project
    fields="__all__"
    success_url = "/management/project-list"
    template_name = "projects/project_form.html"

@method_decorator(staff_member_required,name="dispatch")
class ProjectDeleteView(DeleteView):
    model = Project
    success_url = "/management/project-list"
    template_name = "projects/project_confirm_delete.html"
