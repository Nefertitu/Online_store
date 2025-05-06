from typing import Any

from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    """Команда для очистки данных каталога из базы данных."""

    help = "Deleting data from a database"

    def handle(self, *args: Any, **options: Any) -> None:
        """Основной метод выполнения команды.
        Последовательно удаляет:
        - Все продукты (Product)
        - Все категории (Category)"""

        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Successfully deleted data from database"))
