from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def test_contact(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_contact_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')