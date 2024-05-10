from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home_page, contacts
from catalog.views import index
app_name = CatalogConfig.name

urlpatterns = [
    path('', index),
    path('home_page/', home_page, name='home_page'),
    path('contacts/', contacts, name='contacts'),
]
