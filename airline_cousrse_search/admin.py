from django.contrib import admin

from .models import *


class GmptoCjuOption(admin.ModelAdmin):
    list_display = ['flight_section','arrival_time','departure_time','flight_number','special_fare','normal_fare']

admin.site.register(GmptoCju, GmptoCjuOption)


class GmptoPusOption(admin.ModelAdmin):
    list_display = ['flight_section','arrival_time','departure_time','flight_number','special_fare','normal_fare']

admin.site.register(GmptoPus, GmptoPusOption)


class PustoCjuOption(admin.ModelAdmin):
    list_display = ['flight_section','arrival_time','departure_time','flight_number','special_fare','normal_fare']

admin.site.register(PustoCju, PustoCjuOption)


class PustoGmpOption(admin.ModelAdmin):
    list_display = ['flight_section','arrival_time','departure_time','flight_number','special_fare','normal_fare']

admin.site.register(PustoGmp, PustoGmpOption)


class CjutoGmpOption(admin.ModelAdmin):
    list_display = ['flight_section','arrival_time','departure_time','flight_number','special_fare','normal_fare']

admin.site.register(CjutoGmp, CjutoGmpOption)


class CjutoPusOption(admin.ModelAdmin):
    list_display = ['flight_section','arrival_time','departure_time','flight_number','special_fare','normal_fare']


admin.site.register(CjutoPus, CjutoPusOption)


class CargoAllOption(admin.ModelAdmin):
    list_display = ['cargo_flight_section_test','cargo_arrival_test','cargo_departure_test','cargo_flight_number_test','cargo_special_fare_test','cargo_normal_fare_test']

admin.site.register(CargoAll, CargoAllOption)
