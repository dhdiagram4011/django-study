from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime

# API model list
#account register
#"""
#name
#password
#main_address
#sub_address
#company
#depart
#position
#"""

class Register(models.Model):
    register_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    main_address = models.CharField(max_length=1000)
    sub_address = models.CharField(max_length=1000)
    company = models.CharField(max_length=500)
    depart = models.CharField(max_length=500)
    position = models.CharField(max_length=500)
    class Meta:
        ordering = ('register_created',)






