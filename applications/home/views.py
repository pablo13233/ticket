from django.shortcuts import render

# Create your views here.

def buscar_ticket(request):
    return render(request, 'home/buscar_ticket.html')
