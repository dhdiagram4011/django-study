from django.urls import path
from .views import *


app_name='reg_user'
urlpatterns = [
    path('main/', reg_user_list, name="reg_user_list"),
    path('result/', reg_user_result, name="reg_user_result"),
    path('auth/register', RegistraionAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/users', UserAPI.as_view()),
]
