from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Администрирование записей блога. Позволяет управлять
       записями блога, с возможностью фильтрации и поиска."""

    list_display = ("id", "title", "author", "content", "created_at", "is_published")
    list_filter = ("title", "author", "created_at", "is_published",)
    search_fields = ("title", "author", "content", "created_at", "is_published")

