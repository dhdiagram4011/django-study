from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponse

from .models import *
from .forms import *



class AgreementList(ListView):
    model = Agreement
    template_name = 'register/agreement.html'