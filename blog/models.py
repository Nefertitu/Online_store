from django.db import models

from users.models import User


class Blog(models.Model):
    """Модель блога"""

    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    author = models.CharField(
        max_length=50,
        verbose_name="Автор поста",
        help_text="Введите свое имя (никнейм)",
        blank=True,
        null=True,
        default="Автор не указан",
    )
    content = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        verbose_name="Превью",
        upload_to="blog/photo",
        blank=True,
        null=True,
        help_text="Загрузите изображение",
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )
    is_published = models.BooleanField(default=False)
    counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )
    owner_post = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="owner_post",
    )

    def __str__(self) -> str:
        """Строковое представление поста"""
        return f"Заголовок - {self.title}, дата создания - {self.created_at}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ["title", "content", "created_at", "counter"]

        permissions = [
            ("can_change_post", "Can change post"),
            ("can_delete_post", "Can delete post"),
        ]
