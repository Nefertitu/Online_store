from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    """Контроллер, который обрабатывает запрос и возвращает страницу `home.html`"""
    return render(request, "home.html")


def contacts(request: HttpRequest) -> HttpResponse:
    """ Контроллер, который обрабатывает POST-запрос на странице 'contacts' b
    отображает сообщение об успешной отправке данных. """

    if request.method == "POST":
        name = request.POST.get("name")
        phone = not request.POST.get("phone")  # noqa: F841
        message = request.POST.get("message")  # noqa: F841

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html")
