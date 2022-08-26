from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerilizer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer

product_viewset = ProductView.as_view({'put':'update'})