from typing import Any

from django import forms
from django.forms import BooleanField, ChoiceField
from django.views.generic.base import ContextMixin


class StyleFormMixin(forms.Form):
    """Миксин для стилизации полей формы"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация миксина с настройкой атрибутов виджетов"""
        super().__init__(*args, **kwargs)

        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            elif isinstance(fild, ChoiceField):
                fild.widget.attrs["class"] = "form-select"
            else:
                fild.widget.attrs["class"] = "form-control"


class AdminCheckMixin(ContextMixin):
    """Миксин для проверки принадлежности к группе `admin`"""

    def get_context_data(self, **kwargs: Any) -> Any:
        """Миксин для проверки принадлежности к группе `admin`"""

        context = super().get_context_data(**kwargs)
        if hasattr(self, "request"):
            user = self.request.user
            context["is_admin"] = user.is_authenticated and user.groups.filter(name="admin").exists()
            return context


class ContentManagerCheckMixin(ContextMixin):
    """Миксин для проверки принадлежности к группе `content manager`"""

    def get_context_data(self, **kwargs: Any) -> Any:
        """Миксин для проверки принадлежности к группе `content manager`"""

        context = super().get_context_data(**kwargs)
        if hasattr(self, "request"):
            user = self.request.user
            context["is_content_manager"] = (
                user.is_authenticated and user.groups.filter(name="content manager").exists()
            )
            return context
