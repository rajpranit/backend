from django.db import models

class Product(models.Model):
    product =  models.CharField(max_length=255)
    content = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2 , default=99.99)

    def __str__(self):
        return self.product