from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('<int:index>', views.get_article_by_index),
    path('create', views.create_article)
]
