from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from catalog.models import Product, Contact


def home(request: HttpRequest) -> HttpResponse:
    """Контроллер, который обрабатывает запрос и возвращает страницу `home.html`"""

    products = Product.objects.all().order_by('-created_at')[:5]
    return render(request, "home.html", {'products': products})


def contacts(request: HttpRequest) -> HttpResponse:
    """ Контроллер, который обрабатывает POST-запрос на странице 'contacts' b
    отображает сообщение об успешной отправке данных. """

    contact = Contact.objects.first()
    if request.method == "POST":
        name = request.POST.get("name")
        phone = not request.POST.get("phone")  # noqa: F841
        message = request.POST.get("message")  # noqa: F841

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html", {'contact': contact})
