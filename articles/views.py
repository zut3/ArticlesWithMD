from django.shortcuts import render, redirect
from .models import Article
from services.base_view import base_view
from .forms import ArticleForm
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required


@base_view
def index(request):
    articles = Article.objects.all().order_by("created")
    return render(request, "index.html", {"articles": articles})


@base_view
def get_article_by_index(request, index: int):
    article = Article.objects.get(pk=index)
    return render(request, "page_of_article.html", {"article": article})


@login_required
@base_view
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        form.instance.author_id = request.user.id
        if form.is_valid():
            form.save()
            return redirect("home")
        return HttpResponseBadRequest("form didn't valid!")
    return render(request, "create_article.html", {"form": ArticleForm()})

