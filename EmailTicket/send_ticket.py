import os
from django.core import mail
from django.conf import settings
#from EmailTicket import EmailTicket_defaults


#Airline Ticket Email Send Setting
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = 'rlaehgud21764011@gmail.com'
EMAIL_HOST_PASSWORD = '08425256@kdh'

#settings.configure(EmailTicket_defaults, DEBUG=True)



mail.send_mail('subject','content','Name<rlaehgud21764011@gmail.com>',['rlaehgud21764011@gmail.com'])

#email = EmailMessage(
#    'Subject here',
#    'Here is the message',
#    to = ['dohyoung.kim@rockplace.co.kr'],
#)