from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponse



def RegisterStart(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        return render(request, 'Accounts/register_success.html', {'object':object})
    else:
        form = RegisterForm()
    return render(request, 'Accounts/register.html', {'form':form})


def AirlineLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        return render(request, 'Accounts/register.html', {'object':object})
    else:
        form = LoginForm()
    return render(request, 'Accounts/login.html', {'form':form})


#class RegisterSuccess(ListView):
#    model = Register
#    template_name = 'Accounts/register_success.html'


def RegisterSuccess(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        return render(request, 'Accounts/register_success.html', {'object':object})
    else:
        form = RegisterForm()
    return render(request, 'Accounts/register.html', {'form':form})    
  