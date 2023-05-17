from django.urls import path
from django.shortcuts import render
from menu.models import Item


def MenuPage(request):
    menu = Item.objects.all()
    context = {
        'menu': menu
    }
    return render(request, 'menu.html', context=context)