from django.contrib import admin

# Register your models here.

from .models import Product, Article, Categories, Contactor, SubCategories

admin.site.register(Product)
admin.site.register(Article)
admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Contactor)

