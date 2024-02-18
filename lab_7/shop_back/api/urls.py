from api import views
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products',views.ProductView, basename='api')
router.register('categories',views.CategoryView, basename='api')
router.register('register',views.UserView, basename='api')
urlpatterns = router.urls

# router = DefaultRouter()
# router.register('',views.ProductView,basename='products/')
# urlpatterns = router.urls