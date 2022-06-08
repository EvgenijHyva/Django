from basketapp.models import Basket
from mainapp.models import Product


def get_basket(user: object):
    return None if not user.is_authenticated else Basket.objects.filter(user=user).first()

def get_hot_product() -> Product:
    return Product.objects.all().order_by("?").first()

