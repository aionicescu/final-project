from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect

from event.models import CHOICES, Eveniment
from ticket_site.forms import TicketForm


class Ticket(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    description = models.TextField(max_length=300)
    status = models.CharField(max_length=100, choices=CHOICES)

    active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()
    event = models.ForeignKey(Eveniment, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tickets = models.ManyToManyField(Ticket)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user.username} on {self.date_ordered}"

    class Meta:
        verbose_name_plural = "Orders"


