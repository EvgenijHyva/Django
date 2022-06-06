from django.urls import path
from basketapp.apps import BasketappConfig
from basketapp.views import basket_add, basket_list, basket_remove
app_name = BasketappConfig.name

urlpatterns = (
    path("", basket_list, name="items"),
    path("add/<int:pk>/", basket_add, name="add_item"),
    path("remove/<int:pk>/", basket_remove, name="remove_item")
)