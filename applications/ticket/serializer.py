from rest_framework import serializers
from .models import Ticket, TicketStatus


class TicketSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='status.status')
    class Meta:
        model = Ticket
        fields = ('codigo_ticket', 'title','status')