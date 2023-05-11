from django.db import models


# Create your models here.
class Product(models.Model):
    Name = models.TextField()
    Manufacturer = models.TextField()
    BarCode = models.TextField(blank=True, null=True)
    ProductionDate = models.DateField()
    ExpiryDate = models.DateField()
    Quantity = models.IntegerField()
    Price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.Name)
