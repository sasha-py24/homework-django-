from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True)
    amount_orders = models.PositiveIntegerField(default=0, null=True)




# коли юзер не зайшоі в акк ми його дані зберігаємо тут,
# і коли він робитимете інше замовлення його дані заново не запис
class TemporaryUser(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)