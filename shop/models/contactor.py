from django.db import models

from shop.managers.products import ProductManager
from core.models import TimeStampedMixin



class Contactor(TimeStampedMixin):

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    objects = ProductManager()

