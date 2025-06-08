from catalog.models import Product
from config.settings import CACHE_ENABLED

from django.core.cache import cache


def get_products_from_cache():
    """Получает данные о продуктах из кэша, если кэш пуст,
    получает данные из базы данных"""

    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'products_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


