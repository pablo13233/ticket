from django.urls import path,include
from applications.ticket.views import *
#
# from rest_framework import routers

# router=routers.DefaultRouter()
# router.register(r'ticket', TicketViewSet,'tickets')

app_name = 'ticket_app'

urlpatterns = [
    path('busqueda_ticket/', resultado_busqueda, name='resultado_busqueda'),
    path('api/ticket/search/<kword>', TicketAPIView.as_view()),
]
