from api import models, serializers
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin
class ProductListByCategory(generics.ListAPIView):
    serializer_class = serializers.ProductModelSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return models.Product.objects.filter(category_id=category_id)

class ProductView(ModelViewSet):
    serializer_class = serializers.ProductModelSerializer
    queryset = models.Product.objects.all()
class CategoryView(ModelViewSet):
    serializer_class = serializers.CategoryModelSerializer
    queryset = models.Category.objects.all()

class UserView(CreateModelMixin, GenericViewSet):
    serializer_class = serializers.UserModelSerializer
    queryset = models.User.objects.all()

# class ProductView(ViewSet):
#     def list(self, request):
#         queryset = models.Product.objects.all()
#         serializer = serializers.ProductSerializer(queryset, many=True)
#
#         return Response(serializer.data)
#     def create(self, request):
#         serializer = serializers.ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         product = models.Product.objects.create(**serializer.validated_data)
#         data = serializers.ProductSerializer(product).data
#
#         return Response(data, status=status.HTTP_201_CREATED)
#     def retrieve(self, request, *args,**kwargs):
#         product = models.Product.category(pk)
#         serializer = serializers.ProductSerializer(product)
#
#         return Response(serializer.data)
#     def destroy(self,request, *args, **kwargs):
#         pk = kwargs['pk']
#         product = models.Product.objects.get(pk=pk)
#         product.delete()
#
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def update(self, request, *args, **kwargs):
#         serializer = serializers.ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         pk = kwargs['pk']
#         product = models.Product.objects.get(pk=pk)
#         product.name = serializer.validated_data['name']
#         product.price = serializer.validated_data['price']
#         product.description = serializer.validated_data['description']
#         product.is_active = serializer.validated_data['is_active']
#         product.save()
#
#         data = serializers.ProductSerializer(product).data
#         return Response(data)
#
#         return Response(status=status.HTTP_204_NO_CONTENT)
# class UserView(ViewSet):
#     def create(self, request):
#         serializer = serializers.UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         user = models.User.objects.create(**serializer.validated_data)
#         data = serializers.UserSerializer(user).data
#
#         return Response(data, status=status.HTTP_201_CREATED)
# class CategoryView(ViewSet):
#     def list(self, request):
#         queryset = models.Product.objects.all()
#         serializer = serializers.ProductSerializer(queryset, many=True)
#         return Response(serializer.data)