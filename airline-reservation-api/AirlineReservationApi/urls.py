from django.urls import include, path
from rest_framework import routers
from .views import *
from django.contrib import admin
from django.urls import reverse

admin.site.site_header = 'Reservation Ticketing System API System'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', index, name=index),
=======
    ###path('',include(router.urls)),
    path('', index, name='index'),
>>>>>>> master
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/', register_list, name='register_list'),
    path('user_list/<int:pk>', register_detail, name='register_detail'),
    path('schedule/', schedule_list, name='schedule_list'),
    path('schedule_list/<int:pk>', schedule_detail, name='schedule_detail'),
    #path('',include(router.urls)),
]

