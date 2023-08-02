from django.db import models
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel
import random
import string

class TicketStatus(models.Model):
    status = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.status)

def generate_ticket_code():
    code_length = 6
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(code_length))
class Ticket(TimeStampedModel):
    codigo_ticket = models.CharField(max_length=6, unique = True, blank=True, null=True)
    title = models.CharField(max_length=100,blank=False, null=False)
    status = models.ForeignKey(TicketStatus, related_name="ticket_status", on_delete=models.PROTECT)
    description = models.TextField(max_length=500, default="", blank=False, null=False)
    user_id = models.ForeignKey(User, related_name='ticket_creador', on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.codigo_ticket:
            self.codigo_ticket = generate_ticket_code()
        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return self.codigo_ticket + ' / ' + self.title
