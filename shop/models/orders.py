from django.db import models
from django.db.models import Q, CheckConstraint

from user.models import User
from core.models import TimeStampedMixin
from django.core.mail import send_mail

from django_lifecycle import LifecycleModel, hook, BEFORE_DELETE, AFTER_SAVE, AFTER_CREATE, AFTER_DELETE


class Order(LifecycleModel, TimeStampedMixin):
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

    @hook(AFTER_CREATE)
    def after_save(self):
        if self.user is not None:
            send_mail('New Order',
                      'email_order.html',
                      "sakuzpol@gmail.com",
                      [self.user.email],
                      fail_silently=False)
        elif self.temp_user:
            send_mail('New Order',
                        'email_order.html',
                        "sakuzpol@gmail.com",
                        [self.temp_user.email],
                      fail_silently=False)

        if self.user:
            self.user.amount_orders += 1
            self.user.save()


    @hook(BEFORE_DELETE)
    def before_delete(self):
        if self.user:
            self.user.amount_orders -= 1
            self.user.save()


