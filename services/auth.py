from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from typing import Optional


def register_user(username: str, password: str) -> User:
    """Регистрирует нового пользователя в системе"""
    user = User.objects.create_user(username=username, password=password)
    user.save()
    return user


def get_user(username: str, password: str) -> Optional[User]:
    """Получение пользователя или None"""
    return authenticate(username=username, password=password)

