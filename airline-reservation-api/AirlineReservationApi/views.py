from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from django.http import HttpResponse


### 안내패이지
def index(request):
    return HttpResponse("html webpage TEST!!!")
    #return render(request, 'AirlineReservationApi/readme.html')



class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        register_created = JSONRenderer().render(data)
        name = JSONRenderer().render(data)
        password = JSONRenderer().render(data)
        main_address = JSONRenderer().render(data)
        sub_address = JSONRenderer().render(data)
        company = JSONRenderer().render(data)
        depart = JSONRenderer().render(data)
        position = JSONRenderer().render(data)
        schedule_created = JSONRenderer().render(data)
        arrival_time = JSONRenderer().render(data)
        departure_time = JSONRenderer().render(data)
        navigation_section = JSONRenderer().render(data)
        operating_time = JSONRenderer().render(data)
        airplane_type = JSONRenderer().render(data)


        kwargs['content_type'] = 'application/json'
        super(JSONResponse,self).__init__(name, **kwargs)

@csrf_exempt
def register_list(request):
    if request.method == "GET":
        AirlineReservationApi = Register.objects.all()
        serializer = RegisterSerializer(AirlineReservationApi, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONRenderer().parse(request)
        serializer = RegisterSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def schedule_list(request):
    if request.method == 'GET':
        AirlineReservationApi = Airschedule.objects.all()
        serializer = AirscheduleSerializer(AirlineReservationApi, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONRenderer().parse(request)
        serializer = AirscheduleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status = 201)
        else:
            return JSONResponse(serializer.errors, status = 400)


@csrf_exempt
def register_detail(request,pk):
    try:
        AirlineReservationApi = Register.objects.get(pk=pk)
    except Register.DoesNotExist:
        return HttpResponse(status = 404)
    if request.method == 'GET':
        serializer = RegisterSerializer(AirlineReservationApi)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RegisterSerializer(AirlineReservationApi, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        AirlineReservationApi.delete()
        return HttpResponse(status = 204)


@csrf_exempt
def schedule_detail(request,pk):
    try:
        AirlineReservationApi = Airschedule.objects.get(pk=pk)
    except Airschedule.DoesNotExist:
        return HttpResponse(status = 404)
    if request.method == 'GET':
        serializer = AirscheduleSerializer(AirlineReservationApi)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AirscheduleSerializer(AirlineReservationApi, data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        AirlineReservationApi.delete()
        return HttpResponse(status = 204)




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer






