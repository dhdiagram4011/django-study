from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

# 회원가입시 입력 리스트
##name = models.CharField(max_length=200)
##birth = models.DateField('생년월일')
##email = models.EmailField(max_length=200)
##main_address = models.CharField(max_length=200)
##sub_address = models.CharField(max_length=200)
##cellphone = models.CharField(max_length=200)
##company_name = models.CharField(max_length=200)
##company_depart = models.CharField(max_length=200)
##company_spot = models.CharField(max_length=200)
##created_date = models.DateTimeField(default=timezone.now)
##published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

def RegisterStart(request):
    if request.method == 'GET':
        form = RegisterForm(request.GET)
        return render(request, 'Accounts/register.html', {'form':form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        posts = form.save()
        name = request.POST.get('name',None)
        birth = request.POST.get('birth',None)
        email = request.POST.get('email',None)
        main_address = request.POST.get('main_address',None)
        sub_address = request.POST.get('sub_address',None)
        cellphone = request.POST.get('cellphone',None)
        company_name = request.POST.get('company_name',None)
        company_depart = request.POST.get('company_depart',None)
        company_spot = request.POST.get('company_spot',None)
        created_date = request.POST.get('created_date',None)
        published_date = request.POST.get('published_date',None)
    return redirect('RegisterSuccess')



def RegisterSuccess(request):
    register_lists = Register.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')[:1]
    #register_lists = Register.objects.all()
    return render(request, 'Accounts/register_success.html', {'register_lists':register_lists})



#def RegisterSuccess(ListView):
#    model = Register
#    template_name = 'Accounts/register_success.html'


#def RegisterSuccess(request):
#    if request.method == 'GET':
#        form = RegisterForm(request.GET)
#        return render(request, 'Accounts/register_success.html', {'Register':Register})
#    else:
#        form = RegisterForm()
#    return render(request, 'Accounts/register.html', {'form':form})


def AirlineLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        return render(request, 'Accounts/register.html', {'object':object})
    else:
        form = LoginForm()
    return render(request, 'Accounts/login.html', {'form':form})
