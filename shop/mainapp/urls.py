from django.urls import path
from mainapp.views import index, products, contacts

app_name = "mainapp"

urlpatterns = (
    path("", index, name="index"),
    path("products/", products, name="products"),
    path("products/<category>/", products, name="products_category"),
    path("contacts/", contacts, name="contacts"),
)
