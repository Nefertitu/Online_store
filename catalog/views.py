from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Contact, Product


def home(request: HttpRequest) -> HttpResponse:
    """Контроллер, который обрабатывает запрос и возвращает страницу `home.html`,
    а также информацию о 5-ти последних добавленных товарах"""

    flowers = Product.objects.all()
    context = {"flowers": flowers,}
    return render(request, "flowers_list.html", context)


def contacts(request: HttpRequest) -> HttpResponse:
    """Контроллер, который обрабатывает POST-запрос на странице 'contacts' b
    отображает сообщение об успешной отправке данных. В обычном режиме отображается
    страница с контактными данными и форма для отправки сообщения"""

    contact = Contact.objects.first()
    if request.method == "POST":
        name = request.POST.get("name")
        phone = not request.POST.get("phone")  # noqa: F841
        message = request.POST.get("message")  # noqa: F841

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html", {"contact": contact})


def flower_detail(request, pk):
    flower = get_object_or_404(Product, pk=pk)
    products = Product.objects.all().order_by("-created_at")[:5]
    context = {"flower": flower,
               "products": products,}
    return render(request, "flower_detail.html", context)


