from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, flower_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("base/", home, name="base"),
    # path("", contacts, name="contacts"),
    path("contacts/", contacts, name="contacts"),
    path("base/<int:pk>/", flower_detail, name="flower_detail"),
]
