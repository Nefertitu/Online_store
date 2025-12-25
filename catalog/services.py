from django.core.cache import cache
from django.db.models import QuerySet

from catalog.models import Category, Product
from config.settings import CACHE_ENABLED


class ProductService:

    def get_products_from_cache(self) -> QuerySet[Product]:
        """Получает данные о продуктах из кэша, если кэш пуст,
        получает данные из базы данных"""

        if not CACHE_ENABLED:
            return Product.objects.all()

        key = "products_list"
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products)
        return products

    def get_products_one_category(self, category_slug: str) -> QuerySet[Product]:
        """Получает товары указанной категории, используя кэширование"""

        try:
            category = Category.objects.get(slug=category_slug)

            if not CACHE_ENABLED:
                return Product.objects.filter(category=category).select_related("category")

            key = f"products_category_{category}"
            products = cache.get(key)
            if products is not None:
                return products

            products = Product.objects.filter(category=category).select_related("category")
            cache.set(key, products)
            return products

        except Category.DoesNotExist:
            return Product.objects.none()
