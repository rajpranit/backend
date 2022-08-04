from django.db import models

class Product(models.Model):
    product =  models.CharField(max_length=255)
    content = models.TextField(default=None, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2 , default=99.99, null=True)

    def __str__(self):
        return self.product

    @property
    def product_name(self):
        return 'this is a product'

    def get_discount(self):
        return '122'