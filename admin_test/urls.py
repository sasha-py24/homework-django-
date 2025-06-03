from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index_admin'),
    path('<model_name>/', views.ModelListView.as_view(), name='model_list'),
    path('<model_name>/<int:mod_id>/delete/', views.ModelDeleteView.as_view(), name='model_delete'),
    path('<model_name>/create/', views.ItemCreateView.as_view(), name='model_create'),
    path('<model_name>/<int:mod_id>/update/', views.ItemUpdateView.as_view(), name='model_update'),

]