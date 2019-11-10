from django.db import models

# 회원가입
class Register(models.Model):
    name = models.CharField(max_length=200)
    birth = models.DateField('생년월일')
    email = models.EmailField(max_length=200)
    main_address = models.CharField(max_length=200)
    sub_address = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    company_depart = models.CharField(max_length=200)
    company_spot = models.CharField(max_length=200)


#로그인
class Airline_Login(models.Model):
    email = models.EmailField(max_length=200)
    password = models.IntegerField(max_length=200)





