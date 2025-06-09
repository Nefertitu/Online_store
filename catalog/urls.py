from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductsListView,
    ProductsOneCategoryList,
    ProductUpdateView,
    contacts,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("catalog/", ProductsListView.as_view(), name="product_list"),
    path(
        "catalog/<slug:category_slug>/",
        cache_page(60 * 5)(ProductsOneCategoryList.as_view()),
        name="product_one_category",
    ),
    path("catalog/contacts/", contacts, name="contacts"),
    path("catalog/<int:pk>/detail/", cache_page(60 * 5)(ProductDetailView.as_view()), name="product_detail"),
    path("catalog/create/", ProductCreateView.as_view(), name="product_form"),
    path("catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_confirm_delete"),
]
