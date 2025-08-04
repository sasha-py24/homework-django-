from django.db import models

from user.models import User
from shop.models import Product

class ReviewModal(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)

    text = models.TextField()



