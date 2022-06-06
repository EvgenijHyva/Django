from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, Category, Contacts


def get_basket(user: object) -> list:
    return [] if not user.is_authenticated else Basket.objects.filter(user=user)

def index(request):
    context = {
        "products": Product.objects.all()[:5],
        "basket": get_basket(request.user)
    }
    return render(request, "mainapp/index.html", context)

def products(request, category_id=None):
    category_item = get_object_or_404(Category, pk=category_id) if category_id else {"name": "все"}
    products_category = Product.objects
    product_list = products_category.all() if not category_id else products_category.filter(category=category_id)
    context = {
        "links_menu": Category.objects.all(),
        "products": product_list,
        "category": category_item,
        "basket": get_basket(request.user),
        "hot_product": Product.objects.all().order_by("?").first(),
        "same_products": product_list.order_by("?")[:3]
    }
    if category_id:
        return render(request, "mainapp/products_list.html", context)
    return render(request, "mainapp/products.html", context)

def contacts(request):
    context = {
        "locations": Contacts.objects.filter(is_active=True),
        "basket": get_basket(request.user)
    }
    return render(request, "mainapp/contact.html", context)
