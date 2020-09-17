from django import forms
from .models import Appointment, AppointmentType, WatchModel, WatchType


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('name', 'email', 'appointment_type', 'watch_model', 'watch_type', 'date',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email',
            'appointment_type': '',
            'watch_model': '',
            'watch_type': '',
            'date': 'Date/ Time?',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}'
            else:
                placeholder = placeholders[field]
            self.fields[field].label = False
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'stripe-style-input'
