from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDeleteView, ProductDetailView, ContactsTemplateView, ProductCreateView

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('catalog/create', ProductCreateView.as_view(), name='products_create'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('...', ProductDeleteView.as_view(), name='product_delete')
]
