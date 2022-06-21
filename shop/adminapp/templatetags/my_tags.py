from django.conf import settings
from django import template

register = template.Library()

@register.filter(name="media_for_image")
def media_for_image(path_to_image: str) -> str:
    if not path_to_image:
        concat_with = settings.STATIC_URL if settings.STATIC_URL else "/static/"
        return concat_with + "img/default.jpg"
    optional = settings.MEDIA_URL if settings.MEDIA_URL else "/media/"
    return f"{optional}{path_to_image}"
