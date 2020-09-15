from django.contrib import admin
from .models import AppointmentType, Appointment


class AppointmentTypeAdmin(admin.ModelAdmin):
    
    list_display = (
        'friendly_name',
        'name',
    )

class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'model',
        'type',
        'appointment_type',
        'date',
    )

    ordering = ('date',)


admin.site.register(AppointmentType, AppointmentTypeAdmin)
admin.site.register(Appointment, AppointmentAdmin)