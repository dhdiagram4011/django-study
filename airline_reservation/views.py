from django.shortcuts import render, get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Airline_Reserv
#from .models import Airline_Reservation_Success

from .forms import *
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin

#구간선택에 따른 페이지 라우팅
#제주 - 김포 선택 : airline_cousrse_search/flight_list_cju2gmp.html
#제주 - 부산 선택 : airline_cousrse_search/flight_list_cju2pus.html
#김포 - 제주 선택 : airline_cousrse_search/flight_list_gmp2cju.html
#김포 - 부산 선택 : airline_cousrse_search/flight_list_gmp2pus.html
#부산 - 제주 선택 : airline_cousrse_search/flight_list_pus2cju.html
#부산 - 김포 선택 :  airline_cousrse_search/flight_list_pus2gmp.html




class ReservationList(LoginRequiredMixin, ListView):
    model = Airline_Reserv
    template_name = 'airline_reservation/reservation.html'


class ReservationSuccessList(ListView):
    model = Airline_Reserv
    template_name = 'airline_reservation/reservation_success.html'
    

def ReservationMain(request):
    return render(request, 'airline_reservation/main.html')


def ReservationStartList(request):
    if request.method == 'POST':
        form = ReservationStartForm(request.POST)
        if form.is_valid():
            return render(request, 'airline_reservation/reservation_success.html')
    else:
        form = ReservationStartForm()
    return render(request, 'airline_reservation/reservation_start.html', {'form':form})


def ReservationSuccessList(request):
    if request.method == 'POST':
        form = ReservationSuccessForm(request.POST)
        if form.is_valid():
            return render(request, 'airline_reservation/reservation_success.html')
        else:
            form = ReservationStartForm()
        return render(request, 'airline_reservation/reservation_start.html', {'form':form})
        

