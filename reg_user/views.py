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
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView

from .serializers import (
    reg_userSerializer,
    CreateUserSerializer,
    UserSerializer,
    LoginUserSerializer,
)
from knox.models import AuthToken
from knox.auth import TokenAuthentication

##API
from rest_framework import viewsets, permissions
from .models import *

class reg_userViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = reg_userSerializer

    def get_queryset(self):
        return self.request.user.Reg_user.all().order_by("-created_date")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RegistraionAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
            body = {"message" : "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user" : UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token" : AuthToken.objects.create(user),
            }
        )

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validate_date
        return Response(
            {
            "user" : UserSerializer(
            user, context = self.get_serializer_context()
        ).data,
        "token": AuthToken.objects.create(user),
        }
    )

class UserAPI(generics.RetrieveAPIView):
    permission_classes =  [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

def reg_user_list(request):
    if request.method == 'GET':
        form = reg_user_list_Form(request.GET)
        return render(request,'reg_user/reg_user.html', {'form':form})
    elif request.method == 'POST':
        form = reg_user_list_Form(request.POST)
        posts = form.save()
        id = request.POST.get('id',None)
        email = request.POST.get('email',None)
        created_date = request.POST.get('created_date',None)
        published_date = request.POST.get('published_date',None)
    return redirect('reg_user_result')


def reg_user_result(request):
    reg_user_lists = reg_user.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    print(reg_user_lists)
    #rev_post_lists = rev_post.objects.all()
    return render(request, 'reg_user/reg_result.html', {'reg_user_lists':reg_user_lists})

