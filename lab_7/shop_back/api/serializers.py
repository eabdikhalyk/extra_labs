from rest_framework import serializers
from . import models
class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =models.User
        fields = '__all__'

# class ProductSerializer(serializers.Serializer):
#      id = serializers.IntegerField(required=False)
#      name = serializers.CharField()
#      price = serializers.FloatField()
#      description = serializers.CharField()
#      quantity = serializers.IntegerField()
#      category = serializers.IntegerField()
#      order = serializers.IntegerField()
#      is_active = serializers.BooleanField()
#
# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False)
#     name = serializers.CharField(max_length=255)
#
# class UserSerlializer(serializers.Serializer):
#     username = serializers.CharField()
#     name = serializers.CharField()
#     surname = serializers.CharField()
#     credit_card = serializers.CharField()
#     product = serializers.BooleanField()
#     is_active = serializers.BooleanField()