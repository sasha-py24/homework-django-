from django.db import models
from shop.managers.products import ProductManager
from core.models import TimeStampedMixin
from shop.choices import ColorChoices, MaterialChoices


class Product(TimeStampedMixin):
    category = models.ForeignKey('shop.Categories', related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    sub_category = models.ForeignKey('shop.SubCategories', related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    contactor = models.ForeignKey('shop.Contactor', related_name='products', on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=100, choices=ColorChoices.choices)
    material = models.CharField(max_length=100, choices=MaterialChoices.choices)

    objects = ProductManager()


class Article(TimeStampedMixin):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField()





