from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView

from adminapp.forms import UserAdminEditForm, ProductEditForm, CategoryEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import Category, Product

class DeleteMethodMixin:
    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AccessMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class UserCreateView(AccessMixin, CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = "adminapp/user_form.html"
    extra_context = {
        "title": "Новый"
    }

    def get_success_url(self):
        return reverse_lazy("adminapp:read_user")


class UserListView(ListView):
    model = ShopUser
    template_name = "adminapp/user_list.html"
    paginate_by = 3

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserUpdateView(AccessMixin, UpdateView):
    model = ShopUser
    template_name = "adminapp/user_form.html"
    form_class = UserAdminEditForm
    extra_context = {
        "title": "Редактирование"
    }

    def get_success_url(self):
        return reverse("adminapp:update_user", args=[self.kwargs.get("pk")])


class UserDeleteView(DeleteMethodMixin, AccessMixin, DeleteView):
    model = ShopUser
    template_name = "adminapp/user_delete_confirm.html"

    def get_success_url(self):
        return reverse_lazy("adminapp:read_user")


class CategoryCreateView(AccessMixin, CreateView):
    model = Category
    form_class = CategoryEditForm
    success_url = reverse_lazy("adminapp:categories")
    template_name = "adminapp/category/category_form.html"
    extra_context = {
        "title": "создание"
    }


class CategoryListView(AccessMixin, ListView):
    template_name = "adminapp/category/list.html"

    def get_queryset(self):
        return Category.objects.all().order_by("-is_active")


class CategoryMixin:
    model = Category

    def get_success_url(self):
        return reverse_lazy("adminapp:categories")


class CategoryUpdateView(CategoryMixin, AccessMixin, UpdateView):
    template_name = "adminapp/category/category_form.html"
    form_class = CategoryEditForm


class CategoryDeleteView(DeleteMethodMixin, CategoryMixin, AccessMixin, DeleteView):
    template_name = "adminapp/category/delete_confirm.html"


class CategoryDetailView(AccessMixin, DetailView):
    model = Category
    template_name = "adminapp/products/products_list.html"


class ProductMixin:
    model = Product

    def get_success_url(self):
        category_id = self.get_object().category_id
        return reverse("adminapp:products_list", args=[category_id])

class ProductCreateView(ProductMixin, AccessMixin, CreateView):
    template_name = "adminapp/products/product_form.html"
    form_class = ProductEditForm


class ProductUpdateView(ProductMixin, AccessMixin, UpdateView):
    template_name = "adminapp/products/product_form.html"
    form_class = ProductEditForm


class ProductDeleteView(DeleteMethodMixin, ProductMixin, AccessMixin, DeleteView):
    template_name = "adminapp/products/delete_confirm.html"


class ProductDetailView(ProductMixin, AccessMixin, DetailView):
    template_name = "adminapp/products/detail.html"


# class ProductListView(AccessMixin, ListView):
#    model = Product
#    template_name = "adminapp/products/products_list.html"

#    def get_context_data(self, *args, **kwargs):
#        context_data = super().get_context_data(*args, **kwargs)
#        context_data["category"] = get_object_or_404(Category, pk=self.kwargs.get("pk"))
#        return context_data

#    def get_queryset(self):
#        return super().get_queryset().filter(category_id=self.kwargs.get("pk"))
