from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDeleteView, ProductDetailView, ContactsTemplateView, \
    ProductCreateView, ProductUpdateView, VersionListView, VersionCreateView, VersionUpdateView, VersionDetailView, \
    VersionDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('catalog/create/', ProductCreateView.as_view(), name='products_create'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('versions/<int:pk>', VersionListView.as_view(), name='versions'),
    path('version/', VersionCreateView.as_view(), name='version_create'),
    path('version/<int:pk>/update/', VersionUpdateView.as_view(), name='version_update'),
    path('version/<int:pk>', VersionDetailView.as_view(), name='version_detail'),
    path('versions/<int:pk>/delete/', VersionDeleteView.as_view(), name='version_delete'),
]
