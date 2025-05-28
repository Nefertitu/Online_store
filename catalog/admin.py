from django.contrib import admin

from catalog.forms import CategoryForm
from catalog.models import Category, Contact, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Администрирование категорий продуктов. Позволяет управлять
    категориями, с возможностью фильтрации и поиска."""

    list_display = ("id", "name")
    list_filter = ("name",)
    search_fields = (
        "name",
        "description",
    )
    form = CategoryForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Администрирование продуктов. Включает отображение основных
    характеристик продуктов, фильтрацию по категориям и имени,
    а также поиск по названию и описанию."""

    list_display = ("id", "name", "price", "category")
    list_filter = (
        "category",
        "name",
    )
    search_fields = (
        "name",
        "description",
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Управление контактной информацией.
    Отображает адрес, телефон и email для контактов."""

    list_display = ("address", "phone", "email")
