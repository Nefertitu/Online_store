from typing import Any

from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    """Команда для наполнения каталога тестовыми данными"""

    help = "Add test products to the database and load test data from fixture"

    def handle(self, *args: Any, **options: Any) -> None:
        """Основной метод выполнения команды. Создает категорию
        'Пеларгонии' (если не существует) и добавляет три тестовых продукта.
        Затем загружает дополнительные данные из JSON-фикстуры."""

        category, _ = Category.objects.get_or_create(name="Пеларгонии")

        products: list = [
            {
                "name": "Quantock Classic",
                "description": "Пеларгония с цветками, верхние лепестки которых темно-бордового цвета, нижние лепестки - белые",
                "category": category,
                "price": "1050.00",
            },
            {
                "name": "Patricia Andrea",
                "description": "Пеларгония с бледно-красными, никогда не открывающимися полностью цветками",
                "category": category,
                "price": "970.00",
            },
            {
                "name": "Chocolate Peppermint",
                "description": "Пеларгония с плоскими бархатными листьями с зоной шоколадного цвета. Листья пахнут мятой",
                "category": category,
                "price": "1100.00",
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully added product: {product.name}{product.category}"))
            else:
                self.stdout.write(self.style.WARNING(f"Product already exists: {product.name}{product.category}"))

        call_command("loaddata", "catalog_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
