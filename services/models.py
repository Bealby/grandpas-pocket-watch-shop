from django.db import models


class AppointmentType(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
            verbose_name_plural = 'Appointment Types'

    def __str__(self):
            return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class PocketWatch(models.Model):
    appointment = models.ForeignKey('AppointmentType', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, null=True, blank=True)
    model = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    date = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
            verbose_name_plural = 'Pocket Watches'
    
    def __str__(self):
            return self.name