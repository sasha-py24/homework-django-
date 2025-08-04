from shop.models import Product, Order

from django import forms

CUSTOM_ADMIN_MODELS = [
    Product,

]

ADMIN_MODELS_FORMS = {}
for model in CUSTOM_ADMIN_MODELS:
    class Form(forms.ModelForm):
        class Meta:
            model = model
            fields = '__all__'
    ADMIN_MODELS_FORMS[model] = Form



