from django.urls import path
from .views import (ProductDetailView, ProductListView, product_list, product_detail,
                    manufacturer_list, manufacturer_detail)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('api/products/', product_list, name='api-product-list'),
    path('api/products/<int:pk>/', product_detail, name='api-product-detail'),

    path('api/manufacturers/', manufacturer_list, name='api-manufacturer-list'),
    path('api/manufacturers/<int:pk>/', manufacturer_detail, name='api-manufacturer-detail')

]