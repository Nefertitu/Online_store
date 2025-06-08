import os
import re
from typing import Any, Union

from django.core.exceptions import ValidationError
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile, UploadedFile
from django.forms import ModelForm
from django.template.defaultfilters import filesizeformat

from config import settings
from core.mixins import StyleFormMixin

from .models import Category, Product


class ProductForm(StyleFormMixin, ModelForm):
    """Форма для создания и редактирования экземпляров Product"""

    FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        exclude = [
            "owner",
        ]

    def clean_field(self, field_name: str) -> Any:
        """Общий метод валидации текстовых полей на запрещенные слова"""

        value = self.cleaned_data.get(field_name)

        if not value:
            return value

        re_forbidden = rf'\b({"|".join(re.escape(word) for word in self.FORBIDDEN_WORDS)})\b'
        lower_value = value.lower()
        found_words = []

        for word in self.FORBIDDEN_WORDS:
            if re.search(word, lower_value, re.IGNORECASE):
                found_words.append(word)

        if re.search(re_forbidden, lower_value, re.IGNORECASE):
            raise ValidationError(f'Нельзя использовать запрещенные слова ({", ".join(found_words)}) в названии')
        return value

    def clean_name(self) -> str:
        """Валидация поля name на запрещенные слова"""
        return self.clean_field("name")

    def clean_description(self) -> str:
        """Валидация поля description на запрещенные слова"""
        return self.clean_field("description")

    def clean_price(self) -> float:
        """Валидация поля price"""

        price = self.cleaned_data["price"]
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean_image(self) -> Union[File, UploadedFile]:
        """Валидация загружаемого изображения"""
        image = self.cleaned_data.get("image")

        if not image:
            default_filename = "default.jpg"
            default_path = os.path.join(settings.MEDIA_ROOT, "flowers", "photo", default_filename)

            with open(default_path, "rb") as f:
                return SimpleUploadedFile(name=default_filename, content=f.read(), content_type="image/jpeg")

        if hasattr(image, "content_type"):
            valid_types = ["image/jpeg", "image/png", "image/jpg"]
            max_size = 5 * 1024 * 1024

            if image.content_type not in valid_types:
                raise ValidationError("Недопустимый формат изображения. Разрешены форматы - JPEG, JPG, PNG")

            if image.size > max_size:
                raise ValidationError(
                    f"Файл слишком большой ({filesizeformat(image.size)}). "
                    f"Допустимый размер - до {filesizeformat(max_size)}."
                )

        return image


class ProductModeratorForm(StyleFormMixin, ModelForm):
    """Форма для модераторов продуктов"""

    class Meta:
        model = Product
        fields = ("status",)


class CategoryForm(StyleFormMixin, ModelForm):
    """Форма для работы с категориями товаров"""

    class Meta:
        model = Category
        fields = "__all__"
        # widgets = {"name": forms.Select(choices=Category.CATEGORY_FLOWER_CHOICES)}
