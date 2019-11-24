from django.contrib.auth import get_user_model
from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    #password = forms.CharField(label='패스워드', widget=forms.PasswordInput)
    #repeat_password = forms.CharField(label='패스워드확인', widget=forms.PasswordInput)
    #name = forms.CharField(label='이름')
    #birth = forms.DateField(label='생년월일')
    #email = forms.EmailField(label='이메일')
    #main_address = forms.CharField(label='주소_01')
    #sub_address = forms.CharField(label='주소_02')
    #cellphone = forms.CharField(label='휴대폰번호')
    #company_name = forms.CharField(label='회사명')
    #company_depart = forms.CharField(label='부서')
    #company_spot = forms.CharField(label='직급')

    def clean_repeat_password(self):
        cd = self.cleaned_data
        
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('passowrd not matched!')
        return cd['repeat_password']


    class Meta:
        model = Register
        fields = ('name','birth','email','main_address','sub_address','cellphone','company_name','company_depart','company_spot','password','repeat_password')


class LoginForm(forms.ModelForm):
    name = forms.CharField(label='name')
    password = forms.CharField(label='passowrd', widget=forms.PasswordInput)

    class Meta:
        model = Airline_Login
        fields = ('email','password')
    