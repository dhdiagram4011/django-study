from django import forms
from .models import *

class ReservationStartForm(forms.ModelForm):

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
    OOR = (
        ('편도','편도'),
        ('왕복','왕복'),
    )
    SELECT_SEAT = (
        ('일반석','일반석'),
        ('프레스티지석','프레스티지석'),
    )

    #편도/왕복여부
    one_or_round = forms.ChoiceField(label='편도-왕복', choices=OOR)
    #출발지, 도착지
    start_end = forms.ChoiceField(label='출발지-도착지', choices=START_END_POINT)
    #가는날/오는날
    fine_day = forms.DateTimeField(label='(Fine)가는날')
    comming_day = forms.DateTimeField(label='(Comm)오는날')
    #탑승객 구분
    passenger_classification_adult = forms.IntegerField(label='성인')
    passenger_classification_infant = forms.IntegerField(label='소아')
    passenger_classification_child = forms.IntegerField(label='유아')  
    #좌석등급
    seat_level = forms.ChoiceField(label='좌석등급', choices=SELECT_SEAT)
    #탑승자 이름
    #passenger_name = forms.CharField(label='passenger_name')
    #연락처
    #contect = forms.CharField(label='contect')
    #항공권 번호
    #ticket_number = forms.IntegerField(label='ticket_number')
    #예약번호
    #reservation_number = forms.IntegerField(label='reservation_number')    
    #좌석등급
    #seat_level = forms.CharField(label='seat_level')
    #항공편명
    #flight_name = forms.CharField(label='flight_name')
    #항공기출발시간/도착시간
    #departure_time = forms.DateTimeField(label='departure_time') 
    #arrival_time =  forms.DateTimeField(label='arrival_time')
    #회원/비회원여부
    #member_table = forms.CharField(label='member_table')
    #가격
    #price = forms.IntegerField(label='price')
    #탑승인원
    #passenger_number = forms.IntegerField(label='passenger_number') 
    #항공권예약날짜
    #ticket_reservation_date = forms.DateTimeField(label='ticket_reservation_date')
    #비행시간
    #flight_time = forms.CharField(label='flight_time') 
    #수화물
    #luggage = forms.IntegerField(label='luggage')
    #운임
    #fare = "BLWND"
    #결제수단
    #method_of_payment = forms.CharField(label='method_of_payment') 
    #결제가격
    #payment = forms.IntegerField(label='payment')
    #결제번호
    #billing_number = forms.IntegerField(label='billing_number')

    class Meta:
        model = Airline_Reserv
        fields = ['one_or_round','start_end','fine_day','comming_day','passenger_classification_adult','passenger_classification_infant','passenger_classification_child']


class ReservationSuccessForm(forms.ModelForm):
    #편도/왕복여부
    one_or_round = forms.CharField(label='편도-왕복')
    #출발지, 도착지
    start_end = forms.CharField(label='출발지-도착지')
    #가는날/오는날
    fine_day = forms.ChoiceField(label='(Fine)가는날')
    comming_day = forms.ChoiceField(label='(Comm)오는날')
    #탑승객 구분
    passenger_classification_adult = forms.IntegerField(label='성인')
    passenger_classification_infant = forms.IntegerField(label='소아')
    passenger_classification_child = forms.IntegerField(label='유아')  
    #좌석등급
    seat_level = forms.CharField(label='좌석등급')

    class Meta:
        model = Airline_Reserv
        fields = ['one_or_round','start_end','fine_day','comming_day','passenger_classification_adult','passenger_classification_infant','passenger_classification_child']

