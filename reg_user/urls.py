from django.urls import path
from .views import *

app_name='reg_user'

reg_userlist = reg_userViewSet.as_view({"get":"list", "post" : "create"})

reg_userdetail = reg_userViewSet.as_view(
    {"get" : "retrive", "path":"partical_update", "delete":"destroy"}
)

urlpatterns = [
    path('main/', reg_user_list, name="reg_user_list"),
    path('result/', reg_user_result, name="reg_user_result"),
    path('auth/register/', RegistraionAPI.as_view()),
    path('auth/login/', LoginAPI.as_view()),
    path('auth/user/', UserAPI.as_view()),
    path('api-auth/',include(router.urls)),
]
