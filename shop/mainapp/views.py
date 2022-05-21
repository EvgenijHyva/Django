from django.shortcuts import render

def index(request):
    context = {}
    return render(request, "mainapp/index.html", context)

def products(request):
    context = {}
    return render(request, "mainapp/products.html", context)

def contacts(request):
    context = {}
    return render(request, "mainapp/contact.html", context)
