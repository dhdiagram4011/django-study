from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
import requests
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
import urllib.request
from django import forms


def reg_user_list(request):
    if request.method == 'GET':
        form = reg_user_list_Form(request.GET)
        return render(request,'rev_post/main.html', {'form':form})
    elif request.method == 'POST':
        form = reg_user_list_Form(request.POST)
        posts = form.save()
        id = request.POST.get('id',None)
        email = request.POST.get('email',None)
        created_date = request.POST.get('created_date',None)
        published_date = request.POST.get('published_date',None)
    return redirect ('rev_post_result')


def reg_user_result(request):
    reg_user_lists = reg_user.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    #rev_post_lists = rev_post.objects.all()
    return render(request, 'reg_user/main_result.html', {'reg_user_lists':reg_user_lists})
