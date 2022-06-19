from django.urls import path
from mainapp.apps import MainappConfig
from mainapp.views import index, products, contacts, product

app_name = MainappConfig.name

urlpatterns = (
    path("", index, name="index"),
    path("products/", products, name="products"),
    path("products/<int:category_id>/", products, name="products_category"),
    path("contacts/", contacts, name="contacts"),
    path("product/<int:pk>/", product, name="single_product")
)
