from django.db import models

class ProductQueryset(models.QuerySet):
        pass

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQueryset(model=self.model, using=self._db, hints=self._hints)


    def filter_price(self):
        return self.get_queryset().filter(price__gte=100)
