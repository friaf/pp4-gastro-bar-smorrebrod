from django.urls import path
from . import views
from booking.views import add_booking, view_booking

urlpatterns = [
    path(
        'addbooking/', views.add_booking,
        name='addbooking'
    ),
    path(
       'viewbooking/', views.view_booking,
       name='viewbooking'
    ),
]
