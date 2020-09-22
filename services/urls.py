from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),    
    path('edit_appointment/', views.edit_appointment, name='edit_appointment'),
    path('services_success/', views.services_success, name='services_success'),
]
