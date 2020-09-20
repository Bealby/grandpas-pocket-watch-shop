from django import forms
from .models import Appointment, AppointmentTime, AppointmentType,  \
    WatchModel, WatchType


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        appointment_types = AppointmentType.objects.all()
        friendly_names =  \
            [(c.id, c.get_friendly_name()) for c in appointment_types]
        self.fields['appointment_type'].choices = friendly_names

        watch_models = WatchModel.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in watch_models]
        self.fields['watch_model'].choices = friendly_names

        watch_types = WatchType.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in watch_types]
        self.fields['watch_type'].choices = friendly_names

        self.fields['date'].widget.attrs['class'] = 'datepicker'

        placeholders = {
            'name': 'Full Name',
            'email': 'Email',
            'appointment_type': '',
            'watch_model': '',
            'watch_type': '',
            'date': '',
            'time': '',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'stripe-style-input'

        self.fields['date'].widget.attrs['class'] = 'datepicker'
