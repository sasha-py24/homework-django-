from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'age']

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 12:
            raise forms.ValidationError('age must be more 12')
        return age


class UserLoginForm(AuthenticationForm):
    pass


