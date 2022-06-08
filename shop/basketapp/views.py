from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product

@login_required
def basket_list(request):
    context = {
        "basket_items": Basket.objects.filter(user=request.user),
        "title": "Корзина"
    }
    return render(request, "basketapp/list.html", context)

@login_required
def basket_add(request, pk):
    if "login" in request.META.get("HTTP_REFERER"):
        print(pk)
        return HttpResponseRedirect(reverse("app:single_product", args=[pk]))
    product_item = get_object_or_404(Product, pk=pk)
    basket_item = Basket.objects.filter(product=product_item, user=request.user).first()
    if not basket_item:
        basket_item = Basket(product=product_item, user=request.user)
    basket_item.quantity += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def basket_remove(request, pk):
    Basket.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


