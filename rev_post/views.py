from django.shortcuts import render

from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
#import urllib.requests
import requests
from .forms import *
from django.http import HttpResponse

### input_page

###id = models.CharField(max_length=100, primary_key=True)
###email = models.EmailField(max_length=300)
###created_date = models.DateTimeField(default=timezone.now)
###published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)


def rev_post_list(request):
    if request.method == 'GET':
        form = rev_post_list_Form(request.GET)
        return render(request,'rev_post/main.html', {'form':form})
    elif request.method == 'POST':
        form = rev_post_list_Form(request.POST)
        posts = form.save()
        id = request.POST.get('id',None)
        email = request.POST.get('email',None)
        created_date = request.POST.get('created_date',None)
        published_date = request.POST.get('published_date',None)
    return render('rev_post_result')


def rev_post_result(request):
    rev_post_lists = rev_post.objects.filter(publisehd_date__lte=timezone.now()).order_by('-published_date')[:1]
    return render(request, 'rev_post/main_result.html', {'rev_post_lists':rev_post_lists})





