from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from blog.models import Blog
from django.db.models import QuerySet


class BlogListView(ListView):
    """Класс для отображения списка записей в блоге"""

    model = Blog

    def get_queryset(self) -> QuerySet[Blog]:
        """Добавляет условие об отображении записей блога с отметкой 'is_published'"""
        return super().get_queryset().filter(is_published=True)


class BlogDetailView(DetailView):
    """Класс для детального отображения поста"""

    model = Blog

    def get_object(self, queryset=None):
        """Увеличивает количество просмотров поста при каждом его открытии"""
        self.object = super().get_object(queryset)
        self.object.counter += 1
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        """Дополняет контекст шаблона отображения поста"""
        context = super().get_context_data(**kwargs)
        context["latest_objects"] = Blog.objects.filter(is_published=True).order_by("-created_at")[:5]
        return context


class BlogCreateView(CreateView):
    """Класс для создания новой записи блога (поста)"""

    model = Blog
    fields = ["title", "author", "content", "preview", "is_published", "counter"]
    success_url = reverse_lazy("blogs:blog_list")


class BlogUpdateView(UpdateView):
    """Класс для редактирования поста"""

    model = Blog
    fields = ["title", "author", "content", "preview", "is_published", "counter"]
    success_url = reverse_lazy("blogs:blog_list")

    def get_success_url(self):
        """Возвращает на страницу поста после его редактирования"""
        return reverse("blogs:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    """Класс для удаления поста"""

    model = Blog
    success_url = reverse_lazy("blogs:blog_list")
