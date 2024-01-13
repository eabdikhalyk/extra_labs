from rest_framework import serializers
class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.FloatField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    category_id = serializers.IntegerField()
    is_active = serializers.BooleanField()

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)