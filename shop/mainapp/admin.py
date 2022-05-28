from django.contrib import admin
from mainapp.models import Product, Category, Contacts


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", )
    ordering = ("name", "id",)
    search_fields = ("name", )
    list_display = ("id", "name", "created_at", "updated_at")

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", )
    ordering = ("name", "id",)
    search_fields = ("name", "id", "price", )
    list_display = ("category", "name", "price", "quantity", "updated_at", "id",)

@admin.register(Contacts)
class AdminContact(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", )
    ordering = ("is_active", "city", "address")
    search_fields = ("city", "address", "email", "phone",)
    list_display = ("city", "address", "index", "is_active", "phone", "email")