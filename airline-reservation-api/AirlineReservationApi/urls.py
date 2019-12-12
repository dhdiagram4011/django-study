from django.urls import include, path
from rest_framework import routers
from .views import *
from django.contrib import admin

admin.site.site_header = 'Reservation Ticketing System API System'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', register_list, name='register_list'),
    path('register_list/<int:pk>', register_detail, name='register_detail'),
]

