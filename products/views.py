from rest_framework.response import Response
from .permissions import IsStaffEdittedPermision
from rest_framework import generics, mixins, permissions, authentication
from django.shortcuts import get_object_or_404
from .serializers import ProductSerilizer
from .models import Product
from rest_framework.decorators import api_view

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser , IsStaffEdittedPermision]


    def perform_create(self, serializer):
        # print(serializer.validated_data)
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
        # instance = serializer.save()
        # print(instance)
        # if  instance.content:
        #     instance.content = instance.product
        content = serializer.validated_data.get('content')
        if content is None:
            content='more big mansion'
            serializer.save(content='more big house for me')

product_update_view = ProductUpdateView.as_view()

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

product_delete_view = ProductDeleteView.as_view()






class ProductMixinView( generics.GenericAPIView,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):

    queryset = Product.objects.all()
    serializer_class = ProductSerilizer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        content = serializer.validated_data.get('content')
        if not content:
            content = 'This is my new content'
            serializer.save(content=content);




product_mixin_view = ProductMixinView.as_view()


























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



