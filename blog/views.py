from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from blog.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.counter += 1
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_objects"] = Blog.objects.filter(is_published=True).order_by("-created_at")[:5]
        return context


class BlogCreateView(CreateView):
    model = Blog
    fields = ["title", "author", "content", "preview", "is_published", "counter"]
    success_url = reverse_lazy("blogs:blog_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ["title", "author", "content", "preview", "is_published", "counter"]
    success_url = reverse_lazy("blogs:blog_list")

    def get_success_url(self):
        return reverse("blogs:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blogs:blog_list")