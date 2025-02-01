from django import forms
from .models import Product, Categories


# class ProductCreationForm(forms.Form):
#     name = forms.CharField()
#     description = forms.CharField()
#     price = forms.DecimalField()



class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0 or price > 10000:
            raise forms.ValidationError('price must be between 0 and 10000')
        return price


class CategoriesCreationForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'amount']


    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 20 or len(name) < 0:
            raise forms.ValidationError('name must be 20')
        return name

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 0 or amount > 25:
            raise forms.ValidationError('amount must be between 0 and 25')
        return amount