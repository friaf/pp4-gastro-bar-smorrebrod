from django import forms
from datetime import datetime
from tempus_dominus.widgets import DatePicker
from .models import Booking


class BookingTableForm(forms.ModelForm):
    """ Create form from Model """
    class Meta:
        model = Booking
        fields = [
            'phone_number',
            'booking_time',
            'booking_date',
            'party_size',
            'name',
        ]
        labels = {
            'name': 'Name',
            'phone_number': 'Phone Number',
            'booking_time': 'Time',
            'booking_date': 'Date',
            'party_size': 'Party Size',
        }


def __init__(self, *args, **kwargs):
    """
    Add class, required field and DateTime picker
    to third field.
    """
    super().__init__(*args, **kwargs)
    self.fields['booking_date'].widget.attrs['class'] = 'form-control datepicker-input'
    self.fields['booking_date'].widget = DatePicker()
    self.fields['rbooking_date'].widget.attrs['required'] = 'required'
    self.fields['phone_number'].widget.attrs['required'] = 'required'