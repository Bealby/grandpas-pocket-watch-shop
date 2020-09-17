from django import forms
from .models import Appointment, AppointmentType, WatchModel, WatchType


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        appointment_types = AppointmentType.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in appointment_types]
        self.fields['appointment_type'].choices = friendly_names
        watch_models = WatchModel.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in watch_models]
        self.fields['watch_model'].choices = friendly_names
        watch_types = WatchType.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in watch_types]
        self.fields['watch_type'].choices = friendly_names

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['class'] = 'datepicker'