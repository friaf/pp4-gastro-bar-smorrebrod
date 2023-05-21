from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User


# Choices for Time Slots and capacity
capacity = ((2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10"),
            (12, "12"), (20, "20"))
time_slots = ((1, "1:00pm - 2:50pm"), (2, "3:00pm - 4:50pm"),
              (3, "5:00pm - 6:50pm"), (4, "7:00pm - 8:50pm"),
              (5, "9:00pm - 10:50pm"))


# Table and Booking Model
class Table(models.Model):
    """ Creating Tables Model """
    table_id = models.IntegerField(unique=True)
    table_capacity = models.IntegerField(choices=capacity, default=2)

    class Meta:
        """ Order by table number """
        ordering = ['table_id']

    def __str__(self):
        return str(self.table_id)


class Booking(models.Model):
    """ Creating Booking Model """
    customer = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='booking_guest',
        null=True,
        blank=True
    )
    name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=20)
    booking_time = models.IntegerField(choices=time_slots, default=1)
    party_size = models.IntegerField(default=2)
   
    booking_date = models.DateField()
    booking_table = models.ForeignKey(
        Table, on_delete=models.CASCADE,
        related_name="booked_table",
        null=True,
        blank=True  
    )

    def __str__(self):
        return f"{self.customer} - {self.booking_date} {self.booking_time}"
