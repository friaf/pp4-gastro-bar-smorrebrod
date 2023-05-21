from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Booking, Table
from .forms import BookingTableForm


@login_required
def add_booking(request):
    """
    Creation of booking by customer and adding it to db
    """
    if request.method == 'POST':
        form = BookingTableForm(request.POST)
        if form.is_valid():
            booking = form.save()
            booking.customer = request.user
            booking.save()
            messages.success(request, 'Booking is successful.')
        else:
            messages.error(request, 'Booking date must be in the future.')
    form = BookingTableForm()
    context = {
        'form': form
        }

    return render(request, 'booking.html', context)


@login_required
def view_booking(request):
    """
    Function enables user to view a booking after
    it has been made and added to the database.
    """
    form = BookingTableForm(
        initial={'booking_time': Booking.get_booking_time_display}
        )
    bookings = Booking.objects.filter(customer__in=[request.user])
    context = {
        'bookings': bookings
        }
    return render(request, 'view_booking.html', context)
