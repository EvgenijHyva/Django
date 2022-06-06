from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
        ordering = ("created_at",)
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="добавлен")

    def __str__(self):
        return f"Продукт: {self.product}, количество: {self.quantity}шт"
    
    @property
    def get_price(self):
        return self.quantity * self.product.price