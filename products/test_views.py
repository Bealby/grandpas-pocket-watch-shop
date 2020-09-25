from django.test import TestCase

class TestViews(TestCase):
    def test_products(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'includes/mobile-header.html')
        self.assertTemplateUsed(response, 'includes/main-header.html')
        self.assertTemplateUsed(response, 'includes/main-nav.html')
        self.assertTemplateUsed(response, 'includes/footer.html')
