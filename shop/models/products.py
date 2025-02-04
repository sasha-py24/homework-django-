from django.db import models
from shop.managers.products import ProductManager

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    objects = ProductManager()




class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField()



