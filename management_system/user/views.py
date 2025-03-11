from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm

# Create your views here.
def user_login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request,user)
            print(request.user.first_name)
            return HttpResponseRedirect("management/project-list")
        else:
            return render(request,"login.html",{"message":"Login Failed"})
        
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
        print(form)
        return render(request,"register2.html",{"form":form})
    else:
        form = CustomUserCreationForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(request,"register2.html",{"form":form})