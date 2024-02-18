from django.urls import path
from .views import (
    register_user,
    get_product,
    get_categories,
    get_category_products,
    create_order,
    get_user_orders, user_login,
)

urlpatterns = [
    path('api/login/', user_login, name='user_login'),
    path('api/register/', register_user, name='register_user'),
    path('api/products/<int:product_id>/', get_product, name='get_product'),
    path('api/categories/', get_categories, name='get_categories'),
    path('api/categories/<int:category_id>/products/', get_category_products, name='get_category_products'),
    path('api/product/<int:product_id>/buy/', create_order, name='create_order'),
    path('api/user/<int:user_id>/orders/', get_user_orders, name='get_user_orders'),
]