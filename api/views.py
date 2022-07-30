from itertools import product
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerilizer
# from django.forms.models import model_to_dict
from products.models import Product

@api_view(["GET", 'POST'])
def ApiHome(request, *args, **kwargs):

    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        print(instance.product_name)
        data = ProductSerilizer(instance).data


    return Response(data)