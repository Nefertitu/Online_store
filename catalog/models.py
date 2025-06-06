from django.db import models

from users.models import User


class Category(models.Model):
    """Модель категории товаров"""

    INDOOR_FLOWERS = "Комнатные горшечные растения"
    FUCHSIAS = "Фуксии"
    UZAMBARA_VIOLETS = "Узамбарские фиалки (сенполии)"
    PELARGONIUMS = "Пеларгонии"
    SUCCULENTS = "Суккуленты"

    CATEGORY_FLOWER_CHOICES = [
        (INDOOR_FLOWERS, "Комнатные горшечные растения"),
        (FUCHSIAS, "Фуксии"),
        (UZAMBARA_VIOLETS, "Узамбарские фиалки (сенполии)"),
        (PELARGONIUMS, "Пеларгонии"),
        (SUCCULENTS, "Суккуленты"),
    ]

    name = models.CharField(
        max_length=100,
        choices=CATEGORY_FLOWER_CHOICES,
        default=INDOOR_FLOWERS,
        verbose_name="Наименование",
        help_text="Выберите название категории",
    )
    description = models.TextField(
        verbose_name="Описание", blank=True, null=True, help_text="Введите описание категории"
    )

    def __str__(self) -> str:
        """Строковое представление категории"""
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    """Модель продукта/товара"""

    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"

    STATUS_CHOICES = [(DRAFT, "Черновик"), (PUBLISHED, "Опубликовано"), (ARCHIVED, "В архиве")]

    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите название сорта",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="flowers/photo",
        blank=True,
        null=True,
        help_text="Загрузите изображение",
        unique=False,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        help_text="Выберите категорию",
    )
    price = models.DecimalField(
        verbose_name="Цена за покупку",
        max_digits=20,
        decimal_places=2,
        help_text="Укажите цену",
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        auto_now=True,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text="Выберите статус публикации",
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="owner_product",
        help_text="Владелец продукта (создатель записи)",
    )

    def __str__(self) -> str:
        """Строковое отображение продукта/товара"""
        return f"Наименование: {self.name}, категория: {self.category}, цена - {self.price} рублей."

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "price"]

        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_delete_product", "Can delete product"),
        ]


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
