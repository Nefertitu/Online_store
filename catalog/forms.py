from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    """Форма для создания и редактирования экземпляров Product"""

    class Meta:
        model = Product
        fields = ["name", "description", "category", "price"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }
