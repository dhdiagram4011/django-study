from django.contrib import admin

# Register your models here.
from .models import *

class RegisterOption(admin.ModelAdmin):
    list_display = ['name','birth','email','main_address','sub_address','cellphone','company_name','company_depart','company_spot','created_date','published_date']

admin.site.register(Register, RegisterOption)