from django.shortcuts import render, redirect
from services.auth import register_user, get_user
from django.http import HttpResponseBadRequest, HttpResponse
from services.base_view import base_view
from .forms import UserForm
from django.contrib.auth import logout as log_out, login as login_in_sys


@base_view
def registrate(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = register_user(username, password)
            login_in_sys(request, user)
            return redirect("home")

        return HttpResponse("unvalid")

    return render(request, "registration.html", {"form": UserForm()})


@base_view
def login(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = get_user(username, password)
            if user is None:
                raise Exception(f"User {username} not found!")
            login_in_sys(request, user)
            return redirect("home")
        return HttpResponseBadRequest("unvalid!")

    return render(request, "login.html", {'form': UserForm()})


@base_view
def logout(request):
    log_out(request)
    return redirect("home")
