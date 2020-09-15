from django.db import models


class AppointmentType(models.Model):
    
    class Meta:
            verbose_name_plural = 'Appointment Types'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
            return self.name
            
    def get_friendly_name(self):
            return self.friendly_name
            

class Appointment(models.Model):
    appointment_type = models.ForeignKey('AppointmentType', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, null=True, blank=True)
    model = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    date = models.CharField(max_length=254)

    class Meta:
            verbose_name_plural = 'Appointments'
    
    def __str__(self):
            return self.name