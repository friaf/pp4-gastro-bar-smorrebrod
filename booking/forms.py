from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
from .widget import DatePickerInput, TimePickerInput
from .models import Booking, Table


class BookingTableForm(forms.ModelForm):
    """ Create form from Model """
    class Meta:
        model = Booking
        
        fields = [
            'name',
            'phone_number',
            'party_size',
            'booking_time',
            'booking_date',  
        ]
        widgets = {
            'booking_date': DatePickerInput(),
        }   
        labels = {
            'booking_name': 'Name',
            'number_of_guests': 'Number Of Guests',
            'booking_date': 'Date',
            'booking_time': 'Time',
        }
