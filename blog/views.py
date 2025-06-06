from typing import Any, Optional, Type

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q, QuerySet
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from blog.forms import BlogContentManagerForm, BlogForm
from blog.models import Blog
from core.mixins import ContentManagerCheckMixin


class BlogListView(ContentManagerCheckMixin, ListView):
    """Класс для отображения списка записей в блоге"""

    model = Blog

    def get_queryset(self) -> QuerySet[Blog]:
        """Добавляет условие об отображении записей блога с отметкой 'is_published'"""

        queryset = super().get_queryset()
        user = self.request.user
        if user.is_authenticated:
            return queryset.filter(Q(is_published=True) | Q(owner_post=user))
        return queryset.filter(is_published=True)


class BlogDetailView(DetailView):
    """Класс для детального отображения поста"""

    model = Blog

    def get_object(self, queryset: Optional[QuerySet] = None) -> Blog:
        """Увеличивает количество просмотров поста при каждом его открытии"""
        self.object = super().get_object(queryset)
        self.object.counter += 1
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs: Any) -> dict:
        """Дополняет контекст шаблона отображения поста"""
        context = super().get_context_data(**kwargs)
        context["latest_objects"] = Blog.objects.filter(is_published=True).order_by("-created_at")[:5]
        return context


class BlogCreateView(ContentManagerCheckMixin, LoginRequiredMixin, CreateView):
    """Класс для создания новой записи блога (поста)"""

    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blogs:blog_list")

    def get_form_class(self) -> Type[BlogForm]:
        """Добавляет условие о проверке прав пользователя"""

        user = self.request.user
        if user.is_authenticated:
            return BlogForm
        raise PermissionDenied


class BlogUpdateView(ContentManagerCheckMixin, LoginRequiredMixin, UpdateView):
    """Класс для редактирования поста"""

    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blogs:blog_list")

    def get_success_url(self) -> str:
        """Возвращает на страницу поста после его редактирования"""
        return reverse("blogs:blog_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self) -> Type[BlogContentManagerForm | BlogForm]:
        """Добавляет условие о проверке прав пользователя"""

        user = self.request.user
        if user == self.object.owner_post:
            return BlogForm
        elif user.has_perm("blog.can_change_post"):
            return BlogContentManagerForm
        raise PermissionDenied


class BlogDeleteView(ContentManagerCheckMixin, LoginRequiredMixin, DeleteView):
    """Класс для удаления поста"""

    model = Blog
    success_url = reverse_lazy("blogs:blog_list")

    def get_form_class(self) -> Type[BlogForm]:
        """Добавляет условие о проверке прав пользователя"""

        user = self.request.user
        if user == self.object.owner_post:
            return BlogForm
        elif user.has_perm("blog.can_delete_post"):
            return BlogForm
        raise PermissionDenied
