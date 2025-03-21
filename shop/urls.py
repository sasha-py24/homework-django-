from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('page2/', views.page2, name='page2'),
    path('product/', views.ProductCreationView.as_view(), name='product'),
    path('article/', views.article, name='article'),
    path('product/<int:pk>/details', views.ProductDetailsView.as_view(), name='product_details'),
    path('product/<int:pk>/update', views.ProductUpdateView.as_view(), name='product_update'),
    path('categories/', views.categories, name='categories'),
    path('product/<int:prod_id>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

]