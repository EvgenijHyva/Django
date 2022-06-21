from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.views.generic import DetailView

from mainapp.models import Product, Category, Contacts
from basketapp.services import get_basket, get_hot_product

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

    page_num = request.GET.get("page")
    paginator = Paginator(product_list, per_page=2)
    try:
        paginated_products = paginator.page(page_num)
    except PageNotAnInteger:
        paginated_products = paginator.page(1)
    except EmptyPage:
        paginated_products = paginator.page(paginator.num_pages)
    context = {
        "links_menu": Category.objects.all(),
        "products": paginated_products,
        "category": category_item,
        "basket": get_basket(request.user),
        "hot_product": get_hot_product(),
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


class ProductDetailView(DetailView):
    model = Product
    template_name = "mainapp/product_detail.html"

    extra_context = {
        "links_menu": Category.objects.all(),
    }

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data["basket"] = get_basket(self.request.user)
        return context_data
