from django.test import TestCase
from .forms import AppointmentForm


class TestAppointmentForm(TestCase):
    def test_services_name_is_required(self):
        form = AppointmentForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_services_email_is_required(self):
        form = AppointmentForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_services_appointment_type__is_required(self):
        form = AppointmentForm({'appointment_type': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('appointment_type', form.errors.keys())
        self.assertEqual(form.errors['appointment_type'][0],
                         'This field is required.')

    def test_services_watch_model_is_required(self):
        form = AppointmentForm({'watch_model': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('watch_model', form.errors.keys())
        self.assertEqual(form.errors['watch_model'][0],
                         'This field is required.')

    def test_services_watch_type_is_required(self):
        form = AppointmentForm({'watch_type': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('watch_type', form.errors.keys())
        self.assertEqual(form.errors['watch_type'][0],
                         'This field is required.')

    def test_services_date_is_required(self):
        form = AppointmentForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')

    def test_services_time_is_required(self):
        form = AppointmentForm({'time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(form.errors['time'][0], 'This field is required.')
