from itertools import product
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerilizer
# from django.forms.models import model_to_dict
from django.http import JsonResponse
from products.models import Product

@api_view(["GET", 'POST'])
def ApiHome(request, *args, **kwargs):

    data = request.data
    serializer = ProductSerilizer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
    # return Response(serializer.data)