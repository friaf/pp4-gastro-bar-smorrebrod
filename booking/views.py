from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Booking, Table
from .forms import BookingTableForm


@login_required
def add_booking(request):
    """
    Creation of booking by customer and adding it to db
    """
    form = BookingTableForm()
    if request.method == 'POST':
        form = BookingTableForm(request.POST)
        if form.is_valid():
            booking = form.save()
            booking.customer = request.user
            booking.save()
            messages.success(request, 'Booking is successful.')
            return redirect('viewbooking')
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
    bookings = Booking.objects.filter(customer__in=[request.user])
    context = {
        'bookings': bookings
        }
    return render(request, 'view_booking.html', context)


@login_required
def edit_booking(request, pk):
    booking = Booking.objects.get(id=pk)
    form = BookingTableForm(instance=booking)
    if request.method == 'POST':
        form = BookingTableForm(request.POST, instance)
        if form.is_valid():
            booking = form.save()
            booking.customer = request.user
            booking.save()
            messages.success(request, 'Booking is updated successfuly.')
            return redirect('viewbooking')
    context = {'form': form}
    return render(request, 'booking.html', context)


@login_required
def delete_booking(request, pk):
    booking = Booking.objects.get(id=pk)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking is deleted successfuly.')
        return redirect('viewbooking')   
    context = {'booking': booking}
    return render(request, 'delete_booking.html', context)

