from django.urls import path
from .views import *


app_name  = 'airline_cousrse_search'
## url pattern : http://localhost:8000/reservation_start/cju2gmp/
urlpatterns = [
    path('gmp2cju/',GMP2CJUReservationpage.as_view(), name="GMP2CJUReservation"),
    path('gmp2pus/',GMP2PUSReservationpage.as_view(), name="GMP2PUSReservation"),
    path('pus2cju/',PUS2CJUReservationpage.as_view(), name="PUS2CJUReservation"),
    path('pus2gmp/',PUS2GMPReservationpage.as_view(), name="PUS2GMPReservation"),
    path('cju2gmp/',CJU2GMPReservationpage.as_view(), name="CJU2GMPReservation"),
    path('cargo/' ,CargoReservationpage.as_view(), name="CargoReservation"),
    path('cju2pus/',CJU2PUSReservationpage.as_view(), name="CJU2PUSReservation"),
]