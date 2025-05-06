from django.db import models


class Category(models.Model):
    """Модель категории товаров"""

    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self) -> str:
        """Строковое представление категории"""
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    """Модель продукта/товара"""

    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(verbose_name="Цена за покупку", max_digits=20, decimal_places=2)
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateField(verbose_name="Дата последнего изменения", auto_now=True)

    def __str__(self) -> str:
        """Строковое отображение продукта/товара"""
        return f"Наименование: {self.name}, категория: {self.category}, цена - {self.price} рублей."

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "price"]


class Contact(models.Model):
    """Модель контактов"""

    address = models.CharField(max_length=250, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")

    def __str__(self) -> str:
        """Строковое отображение контактов"""
        return f"Адрес: {self.address}, телефон: {self.phone}, email: {self.email}"

    class Meta:
        verbose_name_plural = "контакты"
