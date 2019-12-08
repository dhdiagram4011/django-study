from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from rest_framework import routers
from reservationapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


admin.site.site_header = 'Reservation Ticketing System'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Accounts.urls')),
    path('/',include('Accounts.urls')),
    path('reservation/',include('airline_reservation.urls')),
    path('reservation_start/', include('airline_cousrse_search.urls')),
    path('agreement/', include('register.urls')),
    path('ticket/', include('Ticketing.urls')),
    #path('e_ticket/',include('EmailTicket.urls')),
    path('rev_post/',include('rev_post.urls')),
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
]
