from django.urls import path
from . import views

urlpatterns = [
    path('articles', views.ArticlesView.as_view()),
    path('articles/new', views.NewArticleView.as_view()),
    path('auth/login', views.Login.as_view()),
    path('auth/registration', views.Registration.as_view()),
]
