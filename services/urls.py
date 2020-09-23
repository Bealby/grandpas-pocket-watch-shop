from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),    
    path('services_success/', views.services_success, name='services_success'),
    path('edit_appointment/<int:appointment_id>/', views.edit_appointment, name='edit_appointment'),
]
