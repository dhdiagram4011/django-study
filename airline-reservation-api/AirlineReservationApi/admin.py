from django.contrib import admin

from django.contrib import admin

from .models import *


class RegisterOption(admin.ModelAdmin):
    list_display = ['register_created','name','password','main_address','sub_address','company','depart','position']

admin.site.register(Register, RegisterOption)



class AirscheduleOption(admin.ModelAdmin):
    list_display = ['schedule_created','arrival_time','departure_time','navigation_section','operating_time','airplane_type']

admin.site.register(Airschedule,AirscheduleOption)




