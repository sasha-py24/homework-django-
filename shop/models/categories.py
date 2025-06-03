from django.db import models
from core.models import TimeStampedMixin
class Categories(TimeStampedMixin):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()


class SubCategories(TimeStampedMixin):
    category = models.ForeignKey('shop.Categories', related_name="sub_categories", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

