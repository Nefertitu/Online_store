from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Category


def categories_processor(request: HttpRequest) -> dict[str, QuerySet[Category] | str | None]:
    """Контекстный процессор для работы с категориями"""

    return {"all_categories": Category.objects.all(), "current_category_slug": request.GET.get("category")}
