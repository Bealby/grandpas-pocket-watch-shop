from django.contrib import admin
from .models import AppointmentType, WatchModel, WatchType, Appointment


class AppointmentTypeAdmin(admin.ModelAdmin):
    
    list_display = (
        'friendly_name',
        'name',
    )


class WatchModelAdmin(admin.ModelAdmin):
    
    list_display = (
        'friendly_name',
        'name',
    )


class WatchTypeAdmin(admin.ModelAdmin):
    
    list_display = (
        'friendly_name',
        'name',
    )


class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        'appointment_type',
        'watch_model',
        'watch_type',
        'name',
        'date',
    )

    ordering = ('date',)


admin.site.register(AppointmentType, AppointmentTypeAdmin)
admin.site.register(WatchModel, WatchModelAdmin)
admin.site.register(WatchType, WatchTypeAdmin)
admin.site.register(Appointment, AppointmentAdmin)