from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    def test_contact_name_is_required(self):
        form = ContactForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_contact_email_is_required(self):
        form = ContactForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_contact_message_is_required(self):
        form = ContactForm({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')
    
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ContactForm()
        self.assertEqual(form.Meta.fields, ['name', 'email', 'message'])
