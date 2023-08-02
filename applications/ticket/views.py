from django.shortcuts import render
from applications.ticket.models import Ticket, TicketStatus
from django.db import transaction
from django.http import JsonResponse, HttpResponse
#
from rest_framework import generics
from .serializer import TicketSerializer


def resultado_busqueda(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                codigo = request.POST['codigoTicket']
                if codigo == '':
                    return JsonResponse({'error': 'error'})
                try:
                    ticket = Ticket.objects.get(codigo_ticket=codigo)
                except Ticket.DoesNotExist:
                    return JsonResponse({'error': 'error'})      
                estado = TicketStatus.objects.get(pk = ticket.status.pk)
        except Exception as e:
            print('Error al buscar ticket--> ',e)
            transaction.rollback()
            return render(request, 'buscar_ticket.html')
        else:
            transaction.commit()
            return JsonResponse({'codigo': ticket.codigo_ticket, 'title': ticket.title, 'estado': estado.status})
        
class TicketAPIView(generics.ListAPIView):
    serializer_class = TicketSerializer
    def get_queryset(self):
        kword = self.kwargs['kword']
        return Ticket.objects.filter(
            codigo_ticket = kword
        )
