##Form

from .models import *
from django import forms


class rev_post_list_Form(forms.ModelForm):
    class Meta:
        model = rev_post
        fields = ('id','email')

