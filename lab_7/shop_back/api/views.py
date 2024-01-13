from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from api import models, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def index(request):
    queryset = models.Product.objects.filter(
        quantity__gt = 0,
        is_active=True,
    )
    serializer = []
    for product in queryset:
        serializer.append(serializers.ProductSerializer(product).data)
    return Response(serializer)
