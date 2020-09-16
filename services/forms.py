from django import forms
from .models import Appointment, AppointmentType, WatchModel, WatchType


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Phone Number',
            'email': 'Email Address',
            'appointment_type': 'Appointment Type',
            'watch_model': 'Watch Model',
            'watch_type': 'Watch Type',
            'date': 'Date',
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        appointment_types = AppointmentType.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in appointment_types]

        self.fields['appointment_type'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        watch_models = WatchModel.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in watch_models]

        self.fields['watch_type'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
