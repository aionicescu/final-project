from django.db import models

from event.models import Event, TicketStatus


class Ticket(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    description = models.TextField(max_length=300)
    status = models.CharField(max_length=100, choices=TicketStatus)

    # active = models.BooleanField(default=True)
    # start_date = models.DateField()
    # end_date = models.DateField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
