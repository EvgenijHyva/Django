from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from adminapp.forms import UserAdminEditForm, ProductEditForm, CategoryEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import Category, Product


@user_passes_test(lambda user: user.is_superuser)
def user_create(request):
    if request.method == "POST":
        edit_form = ShopUserRegisterForm(request.POST, request.FILES)
        if edit_form.is_valid():
            instance = edit_form.save()
            return HttpResponseRedirect(reverse("adminapp:update_user", args=[instance.pk]))
    else:
        edit_form = ShopUserRegisterForm()
    context = {
        "form": edit_form,
        "title": "Новый"
    }

    return render(request, "adminapp/user_form.html", context)


@user_passes_test(lambda user: user.is_superuser)
def user_read(request):
    context = {
        "objects": ShopUser.objects.all().order_by("-is_active", "is_superuser")
    }
    return render(request, "adminapp/user_list.html", context)


@user_passes_test(lambda user: user.is_superuser)
def user_update(request, pk):
    user_item = get_object_or_404(ShopUser, pk=pk)

    if request.method == "POST":
        edit_form = UserAdminEditForm(request.POST, request.FILES, instance=user_item)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("adminapp:update_user", args=[pk]))
    else:
        edit_form = UserAdminEditForm(instance=user_item)
    context = {
        "form": edit_form,
        "title": "Редактирование"
    }

    return render(request, "adminapp/user_form.html", context)


@user_passes_test(lambda user: user.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == "POST":
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse("adminapp:read_user"))
    context = {
        "object": user
    }
    return render(request, "adminapp/user_delete_confirm.html", context)


@user_passes_test(lambda user: user.is_superuser)
def create_category(request):
    if request.method == "POST":
        form = CategoryEditForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("adminapp:categories"))
    else:
        form = CategoryEditForm()
    context = {
        "form": form,
        "title": "создание"
    }
    return render(request, "adminapp/category/category_form.html", context)


@user_passes_test(lambda user: user.is_superuser)
def read_category(request):
    context = {
        "object_list": Category.objects.all().order_by("-is_active")
    }
    return render(request, "adminapp/category/list.html", context)


@user_passes_test(lambda user: user.is_superuser)
def update_category(request, pk):
    category_item = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryEditForm(request.POST, instance=category_item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("adminapp:categories"))
    else:
        form = CategoryEditForm(instance=category_item)
    context = {
        "form": form,
        "category": category_item
    }

    return render(request, "adminapp/category/category_form.html", context)


@user_passes_test(lambda user: user.is_superuser)
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse("adminapp:categories"))
    context = {
        "object": category
    }
    return render(request, "adminapp/category/delete_confirm.html", context)


@user_passes_test(lambda user: user.is_superuser)
def products_list(request, category_pk):
    category_item = get_object_or_404(Category, pk=category_pk)
    product_list = Product.objects.filter(category_id=category_pk)
    context = {
        "objects_list": product_list,
        "category": category_item
    }
    return render(request, "adminapp/products/products_list.html", context)


@user_passes_test(lambda user: user.is_superuser)
def product_create(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    if request.method == "POST":
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            item = product_form.save()
            return HttpResponseRedirect(reverse("adminapp:products_list", args=[item.category.pk]))
    else:
        product_form = ProductEditForm()
    context = {
        "form": product_form,
        "category": category
    }
    return render(request, "adminapp/products/product_form.html", context)


@user_passes_test(lambda user: user.is_superuser)
def products_update(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    if request.method == "POST":
        product_form = ProductEditForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            item = product_form.save()
            return HttpResponseRedirect(reverse("adminapp:products_list", args=[item.category.pk]))
    else:
        product_form = ProductEditForm(instance=product)
    context = {
        "form": product_form,
        "category": product.category
    }
    return render(request, "adminapp/products/product_form.html", context)


@user_passes_test(lambda user: user.is_superuser)
def product_delete(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    if request.method == "POST":
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse("adminapp:products_list", args=[product.category.pk]))
    context = {
        "object": product
    }
    return render(request, "adminapp/products/delete_confirm.html", context)


def products_detail(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    context = {
        "object": product
    }
    return render(request, "adminapp/products/detail.html", context)