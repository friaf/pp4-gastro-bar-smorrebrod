from django.urls import path
from . import views
from menu.views import MenuPage


urlpatterns = [
    path('', views.MenuPage, name='menu'),
]