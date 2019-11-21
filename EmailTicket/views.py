from django.shortcuts import render
import os
from django.core import mail
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.urls import reverse
import reverse


class send_ticket(APIView):
    def post(self, request, format=None):
        email = request.data['email']
        if email is not None:
            subject = 'customer send ticket test'
            message = 'electric ticket'
            mail = EmailMessage(subject, message, to=['dohyoung.kim@rockplace.co.kr'])
            mail.send()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

