from django.contrib import admin
from catalog.models import Product, Category, ContactInfo

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'purchase_price')
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(ContactInfo)

