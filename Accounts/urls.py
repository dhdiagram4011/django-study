from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import *


app_name='Accounts'
urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterStart, name='RegisterStart'),
    path('login/', AirlineLogin, name='logAirlineLogin'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register_success/',RegisterSuccess, name='RegisterSuccess'),
]