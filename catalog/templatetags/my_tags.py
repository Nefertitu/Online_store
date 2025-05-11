from django import template

register = template.Library()


@register.filter()
def media_filter(path: str) -> str:
    """ Генерирует полный URL медиа-файла на основе относительного пути """
    if path:
        return f"/media/{path}"
    return "#"
