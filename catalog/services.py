from config.settings import CACHE_ENABLED
from catalog.models import Product, Category
from django.core.cache import cache

def get_catalog_from_cahe():
    if not CACHE_ENABLED:
        return list(Product.objects.all()())
    key = "product_list" #ключ для кеша
    catalog = cache.get(key) #пытаемся получить данные из кеша
    if catalog is None:

        catalog = list(Product.objects.all())
        cache.set(key, catalog)
    return catalog

def get_cached_categories():
    if not CACHE_ENABLED:
        return list(Category.objects.all())
    key = 'categories_list'
    categories = cache.get(key)
    if categories is None:

        categories = list(Category.objects.all())
        cache.set(key, categories)
    return categories