from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import User
from .forms import UserRegistrationForm, UserLoginForm


def sign_in(request):
    form_u = UserRegistrationForm()
    if request.method == 'POST':
        form_u = UserRegistrationForm(request.POST)
        if form_u.is_valid():
             form_u.save()
        else:
            return render(request, 'user.html', {'form_u': form_u})
    return render(request, 'user.html', {'form_u': form_u})




def log_in(request):
    form_u = UserLoginForm(request)
    if request.method == 'POST':
        form_u = UserLoginForm(request, request.POST)
        print(form_u.is_valid())
        print(form_u.non_field_errors())
        if form_u.is_valid():
            login(request, form_u.user_cache)
            return redirect('index')
    return render(request, 'login.html', {'form_u': form_u})



# def sign_in(request):
#     # if request.method == 'POST':
#     #     username = request.POST['username']
#     #     password = request.POST['password']
#     #     email = request.POST['email']
#     #     user = User(username=username, password=password, email=email)
#     #     user.save()
#     return render(request, 'user.html', {'title': 'sign_in'})