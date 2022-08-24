from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', views.ApiHome, name="apihome")
]
