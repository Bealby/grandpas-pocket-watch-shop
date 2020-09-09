from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_services, name='view_services')
]