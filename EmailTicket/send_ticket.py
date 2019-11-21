import os
from django.core import mail
from django.conf import settings
from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is messages',
    'rlaehgud21764011@gmail.com',
    '[dohyoung.kim@rockplace.co.kr]',
    fail_silently=False,
)









