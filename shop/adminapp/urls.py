from adminapp.apps import AdminappConfig
from django.urls import path
from adminapp import views as adminapp

app_name = AdminappConfig.name

urlpatterns = (
    path("users/create/", adminapp.user_create, name="create_user"),
    path("users/read/", adminapp.user_read, name="read_user"),
    path("users/update/<int:pk>/", adminapp.user_update, name="update_user"),
    path("users/delete/<int:pk>/", adminapp.user_delete, name="delete_user"),

    path("categories/create/", adminapp.create_category, name="create_category"),
    path("categories/read/", adminapp.read_category, name="categories"),
    path("categories/update/<int:pk>/", adminapp.update_category, name="update_category"),
    path("categories/delete/<int:pk>/", adminapp.delete_category, name="delete_category"),

    path("categories/products/read/<int:category_pk>/", adminapp.products_list, name="products_list"),

    path("products/create/<int:category_pk>/", adminapp.product_create, name="create_product"),
    path("products/update/<int:product_pk>/", adminapp.products_update, name="update_product"),
    path("products/delete/<int:product_pk>/", adminapp.product_delete, name="delete_product"),
    path("products/detail/<int:product_pk>/", adminapp.products_detail, name="product_detail")
)
