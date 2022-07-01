from django.urls import path
from . import views

urlpatterns = [
    path("registration", views.registrate, name="reg"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout")
]
