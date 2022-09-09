from rest_framework import serializers
from rest_framework.reverse import reverse
from .validators import validate_title_no_book, unique_product_title
from api.serializers import UserPublicSerializer

from products import validators

from .models import Product

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field = 'pk', read_only= True)
    product = serializers.CharField(read_only = True)


class ProductSerilizer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    # email = serializers.EmailField(write_only=True)
    product = serializers.CharField(validators=[unique_product_title, validate_title_no_book])
    class Meta:
        model = Product
        fields = [
            'pk',
            'owner',
            'related_products',
            'url',
            'edit_url',
            'product',
            'content',
            'price',
            'my_discount'
        ]


    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     print(email, obj)
    #     return obj

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-detail', kwargs={"pk": obj.pk}, request=request)



    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'pk'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount();
