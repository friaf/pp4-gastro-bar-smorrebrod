from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Item(models.Model):
    """ Best Menu Items Model """
    name = models.CharField(max_length=50, unique=True)
    image = CloudinaryField(height_field=None)
  
    def __str__(self):
        return str(self.name)