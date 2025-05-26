import os
import re

from django import forms
from django.forms import BooleanField, ChoiceField, ModelForm

from config import settings
from .models import Product, Category
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template.defaultfilters import filesizeformat


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            if isinstance(fild, ChoiceField):
                fild.widget.attrs['class'] = 'form-select'
            else:
                fild.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, ModelForm):
    """ Форма для создания и редактирования экземпляров Product """
    FORBIDDEN_WORDS = [
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
    ]

    class Meta:
        model = Product
        fields = "__all__"

    def clean_field(self, field_name):
        value = self.cleaned_data.get(field_name)

        if not value:
            return value

        re_forbidden = fr'\b({"|".join(re.escape(word) for word in self.FORBIDDEN_WORDS)})\b'
        lower_value = value.lower()
        found_words = []

        for word in self.FORBIDDEN_WORDS:
            if re.search(word, lower_value, re.IGNORECASE):
                found_words.append(word)

        if re.search(re_forbidden, lower_value, re.IGNORECASE):
            raise ValidationError(f'Нельзя использовать запрещенные слова ({", ".join(found_words)}) в названии')
        return value

    def clean_name(self):
        return self.clean_field('name')

    def clean_description(self):
        return self.clean_field('description')

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if not image:
            default_filename = 'default.jpg'
            default_path = os.path.join(settings.MEDIA_ROOT, 'flowers', 'photo', default_filename)

            with open(default_path, 'rb') as f:
                return SimpleUploadedFile(
                    name=default_filename,
                    content=f.read(),
                    content_type='image/page'
                )

        valid_types = ['image/jpeg', 'image/png', 'image/jpg']
        max_size = 5 * 1024 * 1024

        if image.content_type not in valid_types:
            raise ValidationError('Недопустимый формат изображения. Разрешены форматы - JPEG, JPG, PNG')

        if image.size >= max_size:
            raise ValidationError(
                f'Файл слишком большой ({filesizeformat(image.size)}). '
                f'Допустимый размер - до {filesizeformat(max_size)}.'
            )
        return image

class CategoryForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            'name': forms.Select(choices=Category.CATEGORY_FLOWER_CHOICES)
        }





