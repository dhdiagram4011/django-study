from django.db import models
from django.urls import reverse
from django.utils import timezone

#Airline Ticketing System

class Airline_Reserv(models.Model):

    SELECT_SEAT = (
        ('일반석','일반석'),
        ('프레스티지석','프레스티지석'),
    )

    OOR = (
        ('편도','편도'),
        ('왕복','왕복'),
    )

    MEMBER = (
        ('스카이패스회원','스카이패스회원'),
        ('비회원','비회원'),
    )

    PAYMENT = (
        ('신용카드','신용카드'),
        ('실시간걔좌이체','실시간걔좌이체'),
        ('카카오페이','카카오페이'),
    )

    START_END_POINT = (
        ('김포(GMP) - 부산(PUS)','김포(GMP) - 부산(PUS)'),
        ('김포(GMP) - 제주(CJU)','김포(GMP) - 제주(CJU)'),
        ('부산(PUS) - 제주(CJU)','부산(PUS) - 제주(CJU)'),
        ('부산(PUS) - 김포(GMP)','부산(PUS) - 김포(GMP)'),
        ('제주(CJU) - 김포(GMP)','제주(CJU) - 김포(GMP)'),
        ('제주(CJU) - 부산(PUS)','제주(CJU) - 부산(PUS)'),
    )

    END_END_POINT = (
        ('김포(GMP) - 부산(PUS)','김포(GMP) - 부산(PUS)'),
        ('김포(GMP) - 제주(CJU)','김포(GMP) - 제주(CJU)'),
        ('부산(PUS) - 제주(CJU)','부산(PUS) - 제주(CJU)'),
        ('부산(PUS) - 김포(GMP)','부산(PUS) - 김포(GMP)'),
        ('제주(CJU) - 김포(GMP)','제주(CJU) - 김포(GMP)'),
        ('제주(CJU) - 부산(PUS)','제주(CJU) - 부산(PUS)'),
    )
    

    #출발지, 도착지
    start_end = models.CharField(max_length=200,choices=START_END_POINT, null=False)  
    #탑승자 이름
    passenger_name = models.CharField(max_length=200)
    #탑승객 구분
    passenger_classification_adult = models.IntegerField()
    passenger_classification_infant = models.IntegerField()
    passenger_classification_child = models.IntegerField()
    #연락처
    contect = models.CharField(max_length=200)
    #항공권 번호
    ticket_number = models.IntegerField()
    #예약번호
    reservation_number = models.IntegerField()    
    #좌석등급
    seat_level = models.CharField(max_length=100, choices=SELECT_SEAT, null=False)
    #편도/왕복여부
    one_or_round = models.CharField(max_length=100, choices=OOR)
    #가는날/오는날
    fine_day = models.DateTimeField('(Fine)가는날')
    comming_day = models.DateTimeField('(Comm)오는날')
    #항공편명
    flight_name = models.CharField(max_length=100)
    #항공기출발시간/도착시간
    departure_time = models.DateTimeField(null=False)
    arrival_time = models.DateTimeField(null=False)
    #회원/비회원여부
    member_table = models.CharField(max_length=100, choices=MEMBER, null=False)
    #가격
    price = models.IntegerField()
    #탑승인원
    passenger_number = models.IntegerField() 
    #항공권예약날짜
    ticket_reservation_date = models.DateTimeField(auto_now_add=True)
    #비행시간
    flight_time = models.CharField(max_length=200) 
    #수화물
    luggage = models.IntegerField()
    #운임
    fare = "BLWND"
    #결제수단
    method_of_payment = models.CharField(max_length=100, choices=PAYMENT, null=False) 
    #결제가격
    payment = models.IntegerField()
    #결제번호
    billing_number = models.IntegerField()



    




    