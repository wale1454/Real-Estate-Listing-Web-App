
from distutils.command import upload
from django.db import models

# Create your models here.


class Property(models.Model):

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    price = models.IntegerField()
    Rooms = models.IntegerField()
    imgg = models.ImageField(upload_to='imgs/')

    def __str__ (self):
        return self.name

