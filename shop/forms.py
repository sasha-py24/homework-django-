from django import forms
from .models import Product, Categories, Order, ReviewModal

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



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'temp_user', 'products', 'price']

    def __init__(self, *args, **kwargs):
        self.instance.user = kwargs.pop('user', None)
        self.instance.temp_user = kwargs.pop('temp_user', None)
        self.product = kwargs.pop('product')
        super().__init__(*args, **kwargs)
        self.instance.temp_user = self.temp_user
        self.instance.user = self.user
        self.instance.product = self.product

    def save(self, commit=True):
        instance = super().save(commit)

        return instance


class ProductFilterForm(forms.ModelForm):
    start_price = forms.DecimalField(max_digits=5, decimal_places=2)
    end_price = forms.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        model = Product
        fields = []
    def clean(self):
        pass


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModal
        fields = ['text']
