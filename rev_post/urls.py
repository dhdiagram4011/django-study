from django.urls import path
from .views import *


app_name='rev_post'
urlpatterns = [
    path('main/',rev_post_list, name="rev_result"),
]

