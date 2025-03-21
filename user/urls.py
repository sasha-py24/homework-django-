from django.urls import path

from . import views

urlpatterns = [
    path('sign_in/', views.UserCreationView.as_view(), name='sign_in'),
    path('log_in/', views.LoginPageView.as_view(), name='log_in'),

]