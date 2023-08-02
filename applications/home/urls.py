from django.urls import path
from applications.home.views import *

app_name = 'home_app'

urlpatterns = [
    path('', buscar_ticket, name='buscar_ticket'),
]