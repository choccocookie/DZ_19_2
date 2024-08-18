from django.contrib import admin
from catalog.models import Product, Category, ContactInfo, Version

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'purchase_price',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(ContactInfo)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("product", "version_number", "version_name", "version_attribute")

    list_filter = ('version_attribute', 'product')

