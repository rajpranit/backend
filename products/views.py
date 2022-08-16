from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .serializers import ProductSerilizer
from .models import Product
from rest_framework.decorators import api_view

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer

    def perform_create(self, serializer):
        # print(serializer.validated_data)
        product = serializer.validated_data.get('product')
        content = serializer.validated_data.get('content')
        if content is None:
            content='more big mansion'
            serializer.save(content='more big house')

product_list_create_view = ProductListCreateView.as_view()


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer

product_detail_view = ProductDetailView.as_view()

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        print(instance)
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateView.as_view()



























@api_view(["GET", 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):

    method = request.method
    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerilizer(obj, many=False).data
            return Response(data)
        else:
            queryset = Product.objects.all()
            data = ProductSerilizer(queryset, many=True).data
            return Response(data)
    if method == 'POST':
        print(request.data)
        serializer = ProductSerilizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            product = serializer.validated_data.get('product')
            price = serializer.validated_data.get('price')
            content = serializer.validated_data.get('content') or None

            if content is None :
                serializer.save(content='This is a good content')
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)



