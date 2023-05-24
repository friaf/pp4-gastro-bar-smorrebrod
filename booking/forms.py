from django import forms
from .widget import DatePickerInput
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
        widgets = {
            'booking_date': DatePickerInput(),
        }
        labels = {
            'name': 'Name',
            'phone_number': 'Phone Number',
            'booking_time': 'Time',
            'booking_date': 'Date',
            'party_size': 'Party Size',
        }
