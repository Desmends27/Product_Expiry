from django.urls import path
from .views import create_user, login_user, logout_user

app_name = 'authentication'

urlpatterns = [
    path('create_account/', create_user, name='create_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('', login_user, name='login'),
    path('login/', login_user, name='login'),
]
