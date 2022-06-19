from authapp.forms import ShopUserEditForm, ShopUserRegisterForm
from django import forms

from authapp.models import ShopUser
from mainapp.models import Product


class UserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = "__all__"


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("is_active", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""
