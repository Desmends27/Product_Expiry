from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from product.models import Product


class ProductViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.product = Product.objects.create(
            Name='Test Product',
            Manufacturer='Test Manufacturer',
            ProductionDate='2022-05-10',
            ExpiryDate='2022-06-10',
            Quantity=10,
            Price=20.99,
        )

    def test_add_product_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('product:add_product'), {
            'Name': 'New Test Product',
            'Manufacturer': 'New Test Manufacturer',
            'ProductionDate': '2022-05-11',
            'ExpiryDate': '2022-06-11',
            'Quantity': 20,
            'Price': 25.99,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('product:add_product'))

    def test_edit_product_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('product:edit_product', args=[self.product.pk]), {
            'Name': 'Test Product Edited',
            'Manufacturer': 'Test Manufacturer Edited',
            'ProductionDate': '2022-05-12',
            'ExpiryDate': '2022-06-12',
            'Quantity': 15,
            'Price': 30.99,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('product:edit_product', args=[self.product.pk]))

    def test_products_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('product:products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Test Product')
        self.assertContains(response, 'Test Manufacturer')

    def test_delete_product_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('product:delete_product', args=[self.product.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('product:products'))
