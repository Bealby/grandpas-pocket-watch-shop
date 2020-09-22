from django.db import models

from profiles.models import UserProfile


class AppointmentType(models.Model):
    class Meta:
            verbose_name_plural = 'Appointment Types'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
            return self.name

    def get_friendly_name(self):
            return self.friendly_name


class WatchModel(models.Model):

    class Meta:
            verbose_name_plural = 'Watch Models'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
            return self.name

    def get_friendly_name(self):
            return self.friendly_name


class WatchType(models.Model):

    class Meta:
            verbose_name_plural = 'Watch Types'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
            return self.name

    def get_friendly_name(self):
            return self.friendly_name


class AppointmentTime(models.Model):
    class Meta:
            verbose_name_plural = 'Appointment Times'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
            return self.name

    def get_friendly_name(self):
            return self.friendly_name


class Appointment(models.Model):
    name = models.CharField(max_length=254)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='appointments')
    email = models.EmailField(max_length=70)
    appointment_type = models.ForeignKey('AppointmentType', null=True,
                                         on_delete=models.SET_NULL)
    watch_model = models.ForeignKey('WatchModel', null=True,
                                    on_delete=models.SET_NULL)
    watch_type = models.ForeignKey('WatchType', null=True,
                                   on_delete=models.SET_NULL)
    date = models.DateField()
    time = models.ForeignKey('AppointmentTime', null=True,
                             on_delete=models.SET_NULL)

    class Meta:
            verbose_name_plural = 'Appointments'

    def __str__(self):
            return self.name
