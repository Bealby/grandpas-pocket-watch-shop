from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history,
          name='order_history'),
    path('delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
]
