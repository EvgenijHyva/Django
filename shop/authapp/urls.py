from authapp.apps import AuthappConfig
from django.urls import path
from authapp.views import login, logout, register, edit

app_name = AuthappConfig.name

urlpatterns = (
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path("edit/", edit, name="edit"),
)
