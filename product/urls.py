from django.contrib import admin
from django.urls import path
from .views import products, search, add_product, edit_product

app_name = 'product'

urlpatterns = [
    path('', products, name='products'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:pk>/', edit_product, name='edit_product'),
    path('search/', search, name='search'),
]
