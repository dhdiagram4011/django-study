from django.urls import path
from .views import *


###ReservationStartList = view.py class name


app_name = 'airline_reservation'
urlpatterns = [
    #path('/main',ReservationMain, name='start'),
    path('reservationList/', ReservationList.as_view(), name='reservation'),
    path('reservationStart/', ReservationStartList, name='reservationStart'),
    path('reservationSuccess/', ReservationSuccessList, name='reservationSuccess'),
]