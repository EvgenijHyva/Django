from django.shortcuts import render
import json
def index(request):
    context = {}
    return render(request, "mainapp/index.html", context)

def products(request, category=None):
    context = {}
    links_menu = [
        {"href": "products_all", "title": "Все"},
        {"href": "home", "title": "Дом"},
        {"href": "office", "title": "Офис"},
        {"href": "modern", "title": "Модерн"},
        {"href": "classic", "title": "Классика"},
    ]
    print(category, "category")
    context.update({"links_menu": links_menu})
    return render(request, "mainapp/products.html", context)

def contacts(request):
    context = {}
    with open("mainapp/fixtures/contacts_data.json", "r", encoding="utf-8") as _data:
        data= json.load(_data)
        context.update({"locations": data})
    return render(request, "mainapp/contact.html", context)
