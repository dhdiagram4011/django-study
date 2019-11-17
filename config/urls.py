"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Accounts.urls')),
    path('/',include('airline_reservation.urls')),
    path('reservation/',include('airline_reservation.urls')),
    path('reservation_start/', include('airline_cousrse_search.urls')),
    path('agreement/', include('register.urls')),
    path('ticket/', include('Ticketing.urls')),
]

##Sampels
#urlpatterns  = [
#    path('',views.join, name='join'),
#   path('',views.join_result, name='join_result'),
#    path('',views.translate, name='translate'),
#    path('',views.translate_result, name='translate_result'),
#    path('',views.selecttest, name='selecttest'),
#    path('',views.selecttest_result, name='selecttest_result'),
#    path('',views.main, name='main'),
#    path('',views.radiotest, name='radiotest'),
#    path('',views.login, name='login'),
#    path('',views.login_success, name='login_success'),
#    path('',views.logout, name='logout'),
#    path('',views.serverlist, name='serverlist'),
#]

