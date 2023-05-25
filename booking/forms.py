from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .widget import DatePickerInput
from .models import Booking


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
            'name': 'Name',
            'phone_number': 'Phone Number',
            'booking_time': 'Time',
            'booking_date': 'Date',
            'party_size': 'Party Size',
        }

    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        if booking_date < datetime.today().date():
            raise forms.ValidationError('Date cannot be in passed')
        return booking_date

    def clean_party_size(self):
        party_size = self.cleaned_data.get('party_size')
        if party_size <= 0:
            raise forms.ValidationError('Party size must not be less then 1')
        return party_size
