from django.test import TestCase
from .forms import OrderForm


class TestContactForm(TestCase):
    def test_checkout_full_name_is_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')

    def test_checkout_email_is_required(self):
        form = OrderForm({'email3': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_checkout_phone_number_is_required(self):
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0], 'This field is required.')

    def test_checkout_street_address1_is_required(self):
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0], 'This field is required.')

    def test_checkout_street_address2_is_required(self):
        form = OrderForm({'street_address2': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address2', form.errors.keys())
        self.assertEqual(form.errors['street_address2'][0], 'This field is required.')

    def test_checkout_town_or_city_is_required(self):
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0], 'This field is required.')

    def test_checkout_postcode_is_required(self):
        form = OrderForm({'postcode': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('postcode', form.errors.keys())
        self.assertEqual(form.errors['postcode'][0], 'This field is required.')

    def test_checkout_country_is_required(self):
        form = OrderForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['postcode'][0], 'This field is required.')
    
    def test_checkout_county_is_required(self):
        form = OrderForm({'county': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('county', form.errors.keys())
        self.assertEqual(form.errors['county'][0], 'This field is required.')