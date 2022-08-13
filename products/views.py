from rest_framework import generics
from .serializers import ProductSerilizer
from .models import Product

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        content = serializer.validated_data.get('content')
        if content is None:
            content='more big mansion'
        saved = serializer.save(content='more big house')
        print(saved)

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer
