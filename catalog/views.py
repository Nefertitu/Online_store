from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.models import Contact, Product


class ProductsListView(ListView):
    """Класс для отображения списка всех товаров"""

    model = Product
    paginate_by = 6


class ProductCreateView(CreateView):
    """Класс для создания нового товара"""

    model = Product
    fields = ["name", "description", "image", "category", "price"]
    success_url = reverse_lazy("catalog:product_list")


class ProductDetailView(DetailView):
    """Класс для детального отображения товара"""

    model = Product

    def get_context_data(self, **kwargs: Any) -> dict:
        """Добавляет дополнительные данные в контекст шаблона отображения товара"""
        context = super().get_context_data(**kwargs)
        context["latest_objects"] = Product.objects.filter().order_by("-created_at")[:5]
        return context


class ProductUpdateView(UpdateView):
    """Класс для редактирования существующего товара"""

    model = Product
    fields = ["name", "description", "image", "category", "price"]
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self) -> str:
        """Для отображения детальной страницы товара после её редактирования"""
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    """Класс для удаления товара"""

    model = Product
    success_url = reverse_lazy("catalog:product_list")


def contacts(request: HttpRequest) -> HttpResponse:
    """Контроллер, который обрабатывает POST-запрос на странице 'contacts' и
    отображает сообщение об успешной отправке данных. В обычном режиме отображается
    страница с контактными данными и форма для отправки сообщения"""

    contact = Contact.objects.first()
    if request.method == "POST":
        name = request.POST.get("name")
        phone = not request.POST.get("phone")  # noqa: F841
        message = request.POST.get("message")  # noqa: F841

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "catalog/contacts.html", {"contact": contact})
