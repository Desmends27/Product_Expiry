from django.test import TestCase
from product.models import Product
from product.utilities import search_products


class SearchProductsTestCase(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(Name='Product 1', Manufacturer='Manufacturer 1',
                                               ProductionDate='2022-01-01', ExpiryDate='2023-01-01', Quantity=10,
                                               Price=20.00)
        self.product2 = Product.objects.create(Name='Product 2', Manufacturer='Manufacturer 2',
                                               ProductionDate='2022-02-01', ExpiryDate='2023-02-01', Quantity=20,
                                               Price=30.00)

    def test_search_products_by_name(self):
        query = 'Product 1'
        products = search_products(query)
        self.assertIn(self.product1, products)
        self.assertNotIn(self.product2, products)

    def test_search_products_by_manufacturer(self):
        query = 'Manufacturer 2'
        products = search_products(query)
        self.assertIn(self.product2, products)
        self.assertNotIn(self.product1, products)
