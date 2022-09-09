from rest_framework import serializers



class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField()
    # my_products = serializers.SerializerMethodField(read_only = True)

    # def get_my_products(self, obj):
    #     # request = self.context.get('request')
    #     user = obj
    #     products = user.product_set.all()
    #     return UserProductInlineSerializer(products, many = True,context= self.context).data

