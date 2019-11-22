from django.urls import path
from .views import *


app_name='rev_post'
urlpatterns = [
    path('main/', rev_post_list, name="rev_post_list"),
    path('result/', rev_post_result, name="rev_post_result"),
]

