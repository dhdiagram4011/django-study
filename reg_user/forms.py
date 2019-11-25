##Form
from .models import *
from django import forms


class reg_user_list_Form(forms.ModelForm):
    class Meta:
        model = reg_user
        fields = ('id','email')
