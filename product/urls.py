from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.products, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('search/', views.search, name='search'),
    path('expired/', views.expired_products_view, name='expired_products'),
    path('expiring/<int:days_threshold>/', views.expiring_products_view, name='expiring_products'),
]
