from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator

# def validate_title(value):
#     qs = Product.objects.filter(product__iexact = value)
#     if qs.exists():
#         raise serializers.ValidationError(f"{value} already exists")
#     return value

def validate_title_no_book(value):
    if 'book' in value.lower():
        raise serializers.ValidationError("no book accepted")
    return value
unique_product_title = UniqueValidator(Product.objects.all())