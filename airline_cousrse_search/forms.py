from django import forms
from .models import *


class GMP2CJUReservationForm(forms.ModelForm):
    departure_time = forms.DateTimeField(label="출발시간")
    arrival_time = forms.DateTimeField(label="도착시간")
    flight_section = forms.CharField(label="비행구간",max_length=300)
    flight_number = forms.CharField(label="항공편기종",max_length=300)
    special_fare = forms.IntegerField(label="특별운임")
    normal_fare = forms.IntegerField(label="정상운임") 

    class Meta:
        model = GmptoCju
        fields = ['flight_section','flight_number','departure_time','arrival_time','special_fare','normal_fare']


class GMP2PUSReservationForm(forms.ModelForm):
    departure_time = forms.DateTimeField(label="출발시간")
    arrival_time = forms.DateTimeField(label="도착시간")
    flight_section = forms.CharField(label="비행구간",max_length=300)
    flight_number = forms.CharField(label="항공편기종",max_length=300)
    special_fare = forms.IntegerField(label="특별운임")
    normal_fare = forms.IntegerField(label="정상운임") 

    class Meta:
        model = GmptoPus
        fields = ['flight_section','flight_number','departure_time','arrival_time','special_fare','normal_fare']


class PUS2CJUReservationForm(forms.ModelForm):
    departure_time = forms.DateTimeField(label="출발시간")
    arrival_time = forms.DateTimeField(label="도착시간")
    flight_section = forms.CharField(label="비행구간",max_length=300)
    flight_number = forms.CharField(label="항공편기종",max_length=300)
    special_fare = forms.IntegerField(label="특별운임")
    normal_fare = forms.IntegerField(label="정상운임") 

    class Meta:
        model = PustoCju
        fields = ['flight_section','flight_number','departure_time','arrival_time','special_fare','normal_fare']


class PUS2GMPReservationForm(forms.ModelForm):
    departure_time = forms.DateTimeField(label="출발시간")
    arrival_time = forms.DateTimeField(label="도착시간")
    flight_section = forms.CharField(label="비행구간",max_length=300)
    flight_number = forms.CharField(label="항공편기종",max_length=300)
    special_fare = forms.IntegerField(label="특별운임")
    normal_fare = forms.IntegerField(label="정상운임") 

    class Meta:
        model = PustoGmp
        fields = ['flight_section','flight_number','departure_time','arrival_time','special_fare','normal_fare']


class CJU2GMPReservationForm(forms.ModelForm):
    departure_time = forms.DateTimeField(label="출발시간")
    arrival_time = forms.DateTimeField(label="도착시간")
    flight_section = forms.CharField(label="비행구간",max_length=300)
    flight_number = forms.CharField(label="항공편기종",max_length=300)
    special_fare = forms.IntegerField(label="특별운임")
    normal_fare = forms.IntegerField(label="정상운임") 

    class Meta:
        model = CjutoGmp
        fields = ['flight_section','flight_number','departure_time','arrival_time','special_fare','normal_fare']


class CJU2PUSReservationForm(forms.ModelForm):
    departure_time = forms.DateTimeField(label="출발시간")
    arrival_time = forms.DateTimeField(label="도착시간")
    flight_section = forms.CharField(label="비행구간",max_length=300)
    flight_number = forms.CharField(label="항공편기종",max_length=300)
    special_fare = forms.IntegerField(label="특별운임")
    normal_fare = forms.IntegerField(label="정상운임") 

    class Meta:
        model = CjutoPus
        fields = ['flight_section','flight_number','departure_time','arrival_time','special_fare','normal_fare']
