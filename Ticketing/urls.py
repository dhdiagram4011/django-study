from django.urls import path
from .views import *


###ReservationStartList = view.py class name


##http://localhost:8000/ticket/boarding_ticket_download/
##http://localhost:8000/ticket/b_gmp2cju_dl/ -> 김포 - 제주구간
##http://localhost:8000/ticket/b_gmp2pus_dl/ -> 김포 - 부산구간
##http://localhost:8000/ticket/b_cju2pus_dl/ -> 제주 - 부산구간
##http://localhost:8000/ticket/b_cju2gmp_dl/ -> 제주 - 김포구간
##http://localhost:8000/ticket/b_pus2cju_dl/ -> 부산 - 제주구간
##http://localhost:8000/ticket/b_pus2gmp_dl/ -> 부산 - 김포구간


app_name = 'Ticketing'
urlpatterns = [
    path('boarding/' , boarding, name='boarding'),
    path('boarding_ticket_download/', boarding_ticket_download.as_view(), name="boarding_ticket_download"),
    path('b_gmp2cju_dl/', b_gmp2cju_dl.as_view(), name="b_gmp2cju_dl"),
    path('b_gmp2pus_dl/', b_gmp2pus_dl.as_view(), name="b_gmp2pus_dl"),
    path('b_cju2pus_dl/', b_cju2pus_dl.as_view(), name="b_cju2pus_dl"),
    path('b_cju2gmp_dl/', b_cju2gmp_dl.as_view(), name="b_cju2gmp_dl"),
    path('b_pus2cju_dl/', b_pus2cju_dl.as_view(), name="b_pus2cju_dl"),
    path('b_pus2gmp_dl/', b_pus2gmp_dl.as_view(), name="b_pus2gmp_dl"),
]