from django.contrib import admin
from django.urls import path,include
from client import views
from management_system import settings

urlpatterns = [
    #path('admin/', admin.site.urls),
    # path('',views.home,name="home"),
    path('display-clients/',views.ClientListView.as_view(),name="display-clients"),
    path('client-detail/<str:pk>',views.ClientDetailView.as_view(),name="client-detail"),
    path('register-client/',views.ClientCreateView.as_view(),name="register-client"),
    path('update-client/<str:pk>',views.ClientUpdateView.as_view(),name="update-client"),
    path('delete-client/<str:pk>',views.ClientDeleteView.as_view(),name="delete-client"),
]
