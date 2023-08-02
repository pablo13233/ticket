from django.contrib import admin
from .models import TicketStatus, Ticket

admin.site.register(TicketStatus)
admin.site.register(Ticket)