from django.urls import path
from . import views
from booking.views import *

urlpatterns = [
    path(
        'addbooking/', views.add_booking,
        name='addbooking'
    ),
    path(
       'viewbooking/', views.view_booking,
       name='viewbooking'
    ),
    path(
        'editbooking/<str:pk>/', views.edit_booking,
        name='editbooking'
    ),
    path(
        'deletebooking/<str:pk>/', views.delete_booking,
        name='deletebooking'
    ),   
]
