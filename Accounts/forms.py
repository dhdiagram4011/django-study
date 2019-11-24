from django.contrib.auth import get_user_model
from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='passowrd', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='repeat_passowrd', widget=forms.PasswordInput)
    name = forms.CharField(label='name')
    birth = forms.DateField(label='birth')
    email = forms.EmailField(label='email')
    main_address = forms.CharField(label='main_address')
    sub_address = forms.CharField(label='sub_address')
    cellphone = forms.CharField(label='cellular_phone')
    company_name = forms.CharField(label='company_name')
    company_depart = forms.CharField(label='company_depart')
    company_spot = forms.CharField(label='company_spot')
    created_date = forms.DateTimeField(label='created_date')
    published_date = forms.DateTimeField(label='published_date')

    def clean_repeat_password(self):
        cd = self.cleaned_data
        
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('passowrd not matched!')
        return cd['repeat_password']


    class Meta:
        model = Register
        fields = ['name','birth','email','main_address','sub_address','cellphone','company_name','company_depart','company_spot','password','repeat_password']


class LoginForm(forms.ModelForm):
    name = forms.CharField(label='name')
    password = forms.CharField(label='passowrd', widget=forms.PasswordInput)

    class Meta:
        model = Airline_Login
        fields = ['email','password']
    