from django.contrib import admin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Table, Booking


# Register your models here.
@admin.register(Table)
class AdminTable(admin.ModelAdmin):
    """ Class that views Tables on admin panel"""
    list_display = (
        'table_id',
        'table_capacity',
    )
    list_filter = ('table_id', 'table_capacity')


@admin.register(Booking)
class AdminBooking(admin.ModelAdmin):
    """ Class that views Bookings on admin panel"""
    list_display = (
        'customer',
        'phone_number',
        'booking_time',
        'booking_date',
        'booking_table',
    )
    list_filter = (
        'booking_table', 
        ('booking_date', DateRangeFilter),
        'booking_time',
    )
    search_fields = ['customer', 'booking_table']

