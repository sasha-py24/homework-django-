from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', cache_page(60)(views.IndexView.as_view()), name='index'),
    path('page2/', views.page2, name='page2'),
    path('product/', views.ProductCreationView.as_view(), name='product'),
    path('article/', views.article, name='article'),
    path('product/<int:pk>/details', views.ProductDetailsView.as_view(), name='product_details'),
    path('product/<int:pk>/update', views.ProductUpdateView.as_view(), name='product_update'),
    path('categories/', views.categories, name='categories'),
    path('product/<int:prod_id>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/catalog', views.CatalogView.as_view(), name='product_catalog'),
    path('product/<int:subcategory_id>/catalog/products/', views.ProductListView.as_view(), name='product_list'),
    path('test/', views.HTMXTestView.as_view(), name='htmx-test'),

]