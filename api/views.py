from itertools import product
import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from products.models import Product


def ApiHome(request, *args, **kwargs):

    product_data = Product.objects.all().order_by('?').first()
    data = {}
    if product_data:
        data = model_to_dict(product_data , fields={'id','product','price'})
        json_data_re = json.dumps(data)
        print(data)

    return HttpResponse(json_data_re , headers={"content-type":"application/json"})
