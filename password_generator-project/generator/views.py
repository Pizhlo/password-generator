from django.shortcuts import render
from django.http import HttpResponse
import random
import string
from django.core.handlers.wsgi import WSGIRequest


def home(request: WSGIRequest) -> HttpResponse:
    """Главная страница сайта"""
    return render(request, 'generator/home.html')


def about(request: WSGIRequest) -> HttpResponse:
    """Страница о сайте"""
    return render(request, 'generator/about.html')


def password(request: WSGIRequest) -> HttpResponse:
    """Функция генерации пароля по заданным параметрам"""
    characters = list(string.ascii_lowercase)
    thepassword = ''

    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})
