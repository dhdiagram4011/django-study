from django.contrib.auth import get_user_model
from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
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
    