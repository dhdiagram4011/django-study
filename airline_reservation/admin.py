from django.contrib import admin


from .models import *

class Airline_ReservOption(admin.ModelAdmin):
    list_display = ['start_end','passenger_name','passenger_classification_adult','passenger_classification_infant','passenger_classification_child','contect','ticket_number','reservation_number','seat_level','one_or_round','fine_day','comming_day','flight_name','departure_time','arrival_time','member_table','price','passenger_number','ticket_reservation_date','flight_time','luggage','fare','method_of_payment','payment','billing_number']

admin.site.register(Airline_Reserv, Airline_ReservOption)






