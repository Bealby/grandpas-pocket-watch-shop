from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),    
    path('appointment_success/', views.appointment_success, name='appointment_success'),
    path('edit_appointment/<int:appointment_id>/', views.edit_appointment, name='edit_appointment'),
    path('edit_appointment_success/', views.edit_appointment_success, name='edit_appointment_success'),
]
