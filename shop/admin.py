from django.contrib import admin

# Register your models here.

from .models import Product, Article, Categories

admin.site.register(Product)
admin.site.register(Article)
admin.site.register(Categories)

