from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, index, products_list, product_info
app_name = CatalogConfig.name

urlpatterns = [
    path('', index),
    path('contacts/', contacts, name='contacts'),
    path('base/', products_list, name='base'),
    path('products/<int:pk>/', product_info, name='product_info')
]
