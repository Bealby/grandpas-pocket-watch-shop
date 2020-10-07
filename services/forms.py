from django import forms
from .models import (
    Appointment, AppointmentTime, AppointmentType, WatchModel, WatchType
)


class AppointmentForm(forms.ModelForm):
    class Meta:
        # Fileds to be included in Appointment Booking form
        model = Appointment
        fields = ('name', 'email', 'appointment_type',
                  'watch_model', 'watch_type',
                  'date', 'time',)

    # Friendly names to be used in form
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

        # Date Picker Calendar for booking form
        self.fields['date'].widget.attrs['class'] = 'datepicker'
        # Placeholders for fields
        placeholders = {
            'name': 'Full Name',
            'email': 'Email',
            'appointment_type': '',
            'watch_model': '',
            'watch_type': '',
            'date': '',
            'time': '',
        }

        # Add placeholders and classes.
        # Remove auto-generated labels.
        # Set autofocus on first field.
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'stripe-style-input'
