from django.contrib import admin
from catalog.models import Category, Product, Version


@admin.register(Category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('description', 'name',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'version_title',)
    list_filter = ('name_product',)
