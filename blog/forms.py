from django.forms import ModelForm

from core.mixins import StyleFormMixin

from .models import Blog


class BlogForm(StyleFormMixin, ModelForm):
    """Форма для создания и редактирования экземпляров Product"""

    class Meta:
        model = Blog
        fields = ("title", "author", "content", "preview", "is_published")


class BlogContentManagerForm(StyleFormMixin, ModelForm):
    """Форма контент менеджера для редактирования записей (постов) пользователей"""

    class Meta:
        model = Blog
        fields = (
            "title",
            "content",
            "preview",
            "is_published",
        )
