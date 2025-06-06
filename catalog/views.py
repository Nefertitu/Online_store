from typing import Any, Type

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Contact, Product
from core.mixins import AdminCheckMixin


class ProductsListView(AdminCheckMixin, ListView):
    """ Класс для отображения списка всех товаров """

    model = Product
    paginate_by = 6


    def get_queryset(self) -> QuerySet[Product]:
        """Добавляет условие об отображении продуктов с отметкой 'published'"""
        user = self.request.user
        if user.has_perm("catalog.can_unpublish_product") and user.has_perm("catalog.can_delete_product"):
            return super().get_queryset().all()
        return super().get_queryset().filter(status="published")


class ProductCreateView(AdminCheckMixin, LoginRequiredMixin, CreateView):
    """ Класс для создания нового товара """

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


    def form_valid(self, form: ProductForm) -> HttpResponse:
        """ Обработка валидной формы - привязка продукта к текущему пользователю """

        form.instance.owner = self.request.user
        return super().form_valid(form)


    def get_form_class(self) -> Type[forms.BaseForm]:
        """ Возвращает класс формы в зависимости от прав пользователя """

        user = self.request.user
        if user.groups.filter(name="admin").exists():
            return ProductForm
        raise PermissionDenied


class ProductDetailView(DetailView):
    """ Класс для детального отображения товара """

    model = Product

    def get_context_data(self, **kwargs: Any) -> dict:
        """ Добавляет дополнительные данные в контекст шаблона отображения товара """

        context = super().get_context_data(**kwargs)
        context["latest_objects"] = Product.objects.filter().order_by("-created_at")[:5]
        return context


class ProductUpdateView(AdminCheckMixin, LoginRequiredMixin, UpdateView):
    """ Класс для редактирования существующего товара """

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self) -> str:
        """ Для отображения детальной страницы товара после её редактирования """
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self) -> Type[forms.BaseForm]:
        """ Возвращает класс формы в зависимости от прав пользователя """

        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(AdminCheckMixin, DeleteView):
    """ Класс для удаления товара """

    model = Product
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self) -> Type[forms.BaseForm]:
        """ Возвращает класс формы в зависимости от прав пользователя """

        user = self.request.user
        if user.has_perm("catalog.can_delete_product"):
            return ProductForm
        if user == self.object.owner:
            return ProductForm
        raise PermissionDenied


def contacts(request: HttpRequest) -> HttpResponse:
    """ Контроллер, который обрабатывает POST-запрос на странице 'contacts' и
    отображает сообщение об успешной отправке данных. В обычном режиме отображается
    страница с контактными данными и форма для отправки сообщения """

    contact = Contact.objects.first()
    if request.method == "POST":
        name = request.POST.get("name")
        phone = not request.POST.get("phone")  # noqa: F841
        message = request.POST.get("message")  # noqa: F841

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "catalog/contacts.html", {"contact": contact})
