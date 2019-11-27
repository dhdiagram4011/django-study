from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
#from django.conf import settings
#from django.urls import reverse
#from django.urls import resolvers
#from django.urls import re_path


admin.site.site_header = 'Reservation Ticketing System'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Accounts.urls')),
    path('/',include('Accounts.urls')),
    path('reservation/',include('airline_reservation.urls')),
    path('reservation_start/', include('airline_cousrse_search.urls')),
    path('agreement/', include('register.urls')),
    path('ticket/', include('Ticketing.urls')),
#    path('e_ticket/',include('EmailTicket.urls')),
    path('rev_post/',include('rev_post.urls')),
    path('reg_user/',include('reg_user.urls')),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
]
