from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm

def login(request):
    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == "POST" and login_form.is_valid():
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("app:index"))
    context = {
        "form": login_form,
        "title": "Вход в систему"
    }
    return render(request, "authapp/login.html", context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("app:index"))

def edit(request):
    if request.method == "POST":
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("auth:edit"))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
    context = {
        "form": edit_form,
        "title": "Редактирование профиля"
    }
    return render(request, "authapp/edit.html", context)

def register(request):
    register_form = ShopUserRegisterForm()
    if request.method == "POST":
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse("authapp:login"))

    context = {
        "form": register_form,
        "title": "Регистрация без смс"
    }
    return render(request, "authapp/register.html", context)
