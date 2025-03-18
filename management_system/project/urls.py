"""
URL configuration for management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from project import views


urlpatterns = [  
    path('project-list',views.ProjectListView.as_view(),name="project-list"),
    path('project-detail/<int:pk>',views.ProjectDetailView.as_view(),name="project-detail"),
    path('create-project/',views.ProjectCreateView.as_view(),name="create-project"),
    path('update-project/<int:pk>',views.ProjectUpdateView.as_view(),name="update-project"),
    path('delete-project/<int:pk>',views.ProjectDeleteView.as_view(),name="delete-project"),
]
