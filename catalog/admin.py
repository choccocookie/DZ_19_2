from django.contrib import admin
from catalog.models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category', 'purchase_price')
    list_filter = ('category',)
    search_fields = ('product_name', 'product_description',)

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


