from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from product.models import Product


class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )

        # Create some test products
        self.product1 = Product.objects.create(
            Name='Product 1', Manufacturer='Manufacturer 1',
            ProductionDate='2021-01-01', ExpiryDate='2022-01-01',
            Quantity=10, Price=5.99
        )
        self.product2 = Product.objects.create(
            Name='Product 2', Manufacturer='Manufacturer 2',
            ProductionDate='2021-01-01', ExpiryDate='2022-01-01',
            Quantity=20, Price=4.99
        )

    def test_create_user_view(self):
        response = self.client.get(reverse('authentication:create_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create-user.html')

        # Test creating a new user
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass',
        }
        response = self.client.post(reverse('authentication:create_user'), data=data)
        self.assertEqual(response.status_code, 302)  # redirect to products page

    def test_login_user_view(self):
        response = self.client.get(reverse('authentication:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        # Test logging in with an existing user
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(reverse('authentication:login'), data=data)
        self.assertEqual(response.status_code, 302)  # redirect to products page

        # Test logging in with invalid credentials
        data = {'username': 'testuser', 'password': 'wrongpass'}
        response = self.client.post(reverse('authentication:login'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'Invalid login details')

    def test_logout_user_view(self):
        # Login first
        self.client.login(username='testuser', password='testpass')

        response = self.client.get(reverse('authentication:logout_user'))
        self.assertEqual(response.status_code, 302)  # redirect to login page

        # Check that the user is actually logged out
        response = self.client.get(reverse('product:products'))
        self.assertRedirects(response, reverse('authentication:login'))