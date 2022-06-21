from adminapp.apps import AdminappConfig
from django.urls import path
from adminapp import views as adminapp

app_name = AdminappConfig.name

urlpatterns = (
    path("users/create/", adminapp.UserCreateView.as_view(), name="create_user"),
    path("users/read/", adminapp.UserListView.as_view(), name="read_user"),
    path("users/update/<int:pk>/", adminapp.UserUpdateView.as_view(), name="update_user"),
    path("users/delete/<int:pk>/", adminapp.UserDeleteView.as_view(), name="delete_user"),

    path("categories/create/", adminapp.CategoryCreateView.as_view(), name="create_category"),
    path("categories/read/", adminapp.CategoryListView.as_view(), name="categories"),
    path("categories/update/<int:pk>/", adminapp.CategoryUpdateView.as_view(), name="update_category"),
    path("categories/delete/<int:pk>/", adminapp.CategoryDeleteView.as_view(), name="delete_category"),

    path("categories/products/read/<int:pk>/", adminapp.CategoryDetailView.as_view(), name="products_list"),

    path("products/create/<int:pk>/", adminapp.ProductCreateView.as_view(), name="create_product"),
    path("products/update/<int:pk>/", adminapp.ProductUpdateView.as_view(), name="update_product"),
    path("products/delete/<int:pk>/", adminapp.ProductDeleteView.as_view(), name="delete_product"),
    path("products/detail/<int:pk>/", adminapp.ProductDetailView.as_view(), name="product_detail")
)
