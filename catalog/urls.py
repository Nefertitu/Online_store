from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, flower_detail, add_new_product, success_view

app_name = CatalogConfig.name

urlpatterns = [
    path("base/", home, name="base"),
    path("contacts/", contacts, name="contacts"),
    path("base/<int:pk>/", flower_detail, name="flower_detail"),
    path("add_product/", add_new_product, name="add_product"),
    path("success/", success_view, name="success_page"),
]
