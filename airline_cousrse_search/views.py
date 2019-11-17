from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import *
from .forms import *
from airline_reservation.models import *
from airline_cousrse_search.models import *
from django.db.models import Q
from django.template import loader

def cju2pus(request):
    return render(request, 'airline_course_search/flight_list_cju2pus.html', {'cju2pus':cju2pus})

def gmp2cju(request):
    return render(request, 'airline_course_search/flight_list_gmp2cju.html', {'gmp2cju':gmp2cju})
    
def gmp2pus(request):
    return render(request, 'airline_course_search/flight_list_gmp2pus.html', {'gmp2pus':gmp2pus})
      
def pus2gmp(request):
    return render(request, 'airline_course_search/flight_list_pus2gmp.html', {'pus2gmp':pus2gmp})
    
def cju2gmp(request):
    return render(request, 'airline_course_search/flight_list_cju2gmp.html', {'cju2gmp':cju2gmp})

def pus2cju(request):
    return render(request, 'airline_course_search/flight_list_pus2cju.html', {'pus2cju':pus2cju})

#def cargoAll(request):
#    return render(request, 'airline_course_search/all_full_time.html', {'cargoAll':cargoAll})


##DB Value
#cargo_departure_test = models.DateTimeField()
#cargo_arrival_test = models.DateTimeField()
#cargo_flight_section_test = models.CharField(choices=SECTION, max_length=300)
#cargo_flight_number_test = models.CharField(choices=EMPHYSEMA, max_length=300)
#cargo_special_fare_test = models.IntegerField()
#cargo_normal_fare_test = models.IntegerField()



def cargo(request):
    #object = CargoAll.objects.filter(cargo_flight_section_test__contains='(PUS)')
    cargo_list = CargoAll.objects.filter(cargo_flight_section_test__contains="PUS")
    template = loader.get_template('airline_course_search/all_full_time.html')
    context = {
        'cargo_list' : cargo_list,
    }
    return HttpResponse(template.render(context, request))
    #return render(request, 'airline_course_search/all_full_time.html', {'object':object})


#def cargoResult(request):
#    cargoResult = cargoAll.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:1]
#    return render(request, 'testapp/serverlist_result.html', {'cargoResults':cargoResults})



#class name

#통합검색
#def airline_schedule_all(request):
#    queryset = GmptoCju.objects.all()
#    query = request.GET.get('김포(GMP)-제주(CJU)','')
#    if GMP2CJUReservationpage:
#        queryest = queryset.filter(title__icontains=GMP2CJUReservationpage)
#    return render(request, 'airline_course_search/flight_list_gmp2pus.html', {'airline_schedule_all' : queryset})

    
## 각 구간별 템플릿 페이지 보여주기 ##
# 각 구간에 대한 스케쥴 출력

#제주 - 김포구간
class CJU2PUSReservationpage(ListView):
    model = CjutoPus
    template_name = 'airline_course_search/flight_list_cju2pus.html'


#김포 - 제주구간
class GMP2CJUReservationpage(ListView):
    model = GmptoCju
    template_name = 'airline_course_search/flight_list_gmp2cju.html'


#김포 - 부산구간
class GMP2PUSReservationpage(ListView):
    model = GmptoPus
    template_name = 'airline_course_search/flight_list_gmp2pus.html'


#부산 - 제주구간
class PUS2CJUReservationpage(ListView):
    model = PustoCju
    template_name = 'airline_course_search/flight_list_pus2cju.html'

#부산 - 김포구간
class PUS2GMPReservationpage(ListView):
    model = PustoGmp
    template_name = 'airline_course_search/flight_list_pus2gmp.html'

#제주 - 김포구간
class CJU2GMPReservationpage(ListView):
    model = CjutoGmp
    template_name = 'airline_course_search/flight_list_cju2gmp.html'

#힝공 스케쥴 전체 리스트 조회
class CargoReservationpage(ListView):
    model = CargoAll
    template_name = 'airline_course_search/airline_full_time.html'

    






    