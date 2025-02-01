from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page2/', views.page2, name='page2'),
    path('product/', views.product, name='product'),
    path('article/', views.article, name='article'),
    path('product/<int:id>/details', views.product_details, name='product_details'),
    path('categories/', views.categories, name='categories'),

]