from django.db import models
from django.db.models import Q, CheckConstraint

from user.models import User
from core.models import TimeStampedMixin


class Order(TimeStampedMixin):
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True,blank=True )
    temp_user = models.ForeignKey('user.TemporaryUser', on_delete=models.SET_NULL, null=True,blank=True)
    products = models.ManyToManyField('shop.Product', related_name='orders', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        constraints = [
          CheckConstraint(check=(
            (Q(user__isnull=False) & Q(temp_user__isnull=True)) |
            (Q(user__isnull=True) & Q(temp_user__isnull=False))
                ), name="one_of_user_must_be_passed")
         ]