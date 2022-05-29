from django.shortcuts import render
from mainapp.models import Product, Category, Contacts


def index(request):
    context = {
        "products": Product.objects.all()[:5]
    }
    return render(request, "mainapp/index.html", context)

def products(request, category_id=None):
    products_category = Product.objects
    context = {
        "links_menu": Category.objects.all(),
        "products": products_category.all() if not category_id else products_category.filter(category=category_id)
    }
    return render(request, "mainapp/products.html", context)

def contacts(request):
    context = {
        "locations": Contacts.objects.filter(is_active=True)
    }
    return render(request, "mainapp/contact.html", context)
