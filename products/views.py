from rest_framework import generics
from .serializers import ProductSerilizer
from .models import Product

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        content = serializer.validated_data.get('content')
        if content is None:
            content='more big mansion'
        serializer.save(content='more big house')

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer
