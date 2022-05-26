from core.models import TimeStampedModel
from django.db import models

class Category(TimeStampedModel):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name", "pk")

    name = models.CharField(max_length=64, verbose_name="Название", unique=True)
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return f"{self.pk} {self.name}"


class Product(TimeStampedModel):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("name", "pk")

    name = models.CharField(max_length=128, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание", blank=True)
    short_desc = models.CharField(verbose_name="Краткое описание", max_length=128)
    image = models.ImageField(upload_to="product", blank=True, null=True, verbose_name="Изображения")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return f"{self.name} ({self.category.pk}:{self.category.name})"


class Contacts(TimeStampedModel):
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ("city", "pk")

    city = models.CharField(max_length=64, verbose_name="Город")
    phone = models.PositiveBigIntegerField(blank=True, null=True, verbose_name="Телефон")
    address = models.CharField(max_length=128, blank=True, null=True, verbose_name="Адресс", unique=True,)
    index = models.PositiveIntegerField(blank=True, null=True, verbose_name="индекс", default="индекс не указан")
    email = models.EmailField(max_length=254, verbose_name="Электронный адрес")
    is_active = models.BooleanField(default=True, verbose_name="Действующий")

    def __str__(self):
        return f"{self.city}, {self.address} - {self.phone}"

    @property
    def get_address(self):
        return f"{self.address}, {self.city}, {self.index}"

    @property
    def get_phone(self):
        return f"+{self.phone}"
