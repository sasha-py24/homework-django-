from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, HttpResponseRedirect


from .models import User, TemporaryUser
from .forms import UserRegistrationForm, UserLoginForm, TempUserForm


class UserCreationView(CreateView):
    template_name = 'user.html'
    model = User
    form_class = UserRegistrationForm
    success_url = '/'


class LoginPageView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True
    success_url = '/'


class TempUserView(CreateView):
    template_name = 'temp_user.html'
    model = TemporaryUser
    form_class = TempUserForm

    def render_to_response(self, context, **response_kwargs):
        html = render_to_string(self.template_name, context, request=self.request)
        return JsonResponse({'html': html})


    def form_valid(self, form):
        form.save()
        self.request.session()
        return JsonResponse({})





class ProfileView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


# def log_in(request):
#     form_u = UserLoginForm(request)
#     if request.method == 'POST':
#         form_u = UserLoginForm(request, request.POST)
#         print(form_u.is_valid())
#         print(form_u.non_field_errors())
#         if form_u.is_valid():
#             login(request, form_u.user_cache)
#             return redirect('index')
#     return render(request, 'login.html', {'form_u': form_u})









# def sign_in(request):
#     form_u = UserRegistrationForm()
#     if request.method == 'POST':
#         form_u = UserRegistrationForm(request.POST)
#         if form_u.is_valid():
#              form_u.save()
#         else:
#             return render(request, 'user.html', {'form_u': form_u})
#     return render(request, 'user.html', {'form_u': form_u})

# def sign_in(request):
#     # if request.method == 'POST':
#     #     username = request.POST['username']
#     #     password = request.POST['password']
#     #     email = request.POST['email']
#     #     user = User(username=username, password=password, email=email)
#     #     user.save()
#     return render(request, 'user.html', {'title': 'sign_in'})