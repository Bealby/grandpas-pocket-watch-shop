from django.contrib import admin
from .models import AppointmentType, PocketWatch


class AppointmentTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class PocketWatchAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'model',
        'type',
        'appointment',
        'date',
    )

    ordering = ('date',)


admin.site.register(AppointmentType, AppointmentTypeAdmin)
admin.site.register(PocketWatch, PocketWatchAdmin)