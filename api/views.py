from itertools import product
from math import prod
from django.http import JsonResponse
from products.models import Product


def ApiHome(request, *args, **kwargs):

    product_data = Product.objects.all().order_by('?').first()
    data = {}
    if product_data:
        data['id'] = product_data.id
        data['title'] = product_data.product
        data['content'] = product_data.content
        data['price'] = product_data.price

    return JsonResponse(data)
