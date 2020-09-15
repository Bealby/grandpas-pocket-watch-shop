from django import forms
from .models import Appointment, AppointmentType


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        appointment_types = AppointmentType.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in appointment_types]

        self.fields['appointment_type'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'