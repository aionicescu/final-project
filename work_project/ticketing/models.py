from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect

from event.models import CHOICES, Eveniment


# class Ticket(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField(max_length=30)
#     description = models.TextField(max_length=300)
#     status = models.CharField(max_length=100, choices=CHOICES)
#
#     active = models.BooleanField(default=True)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     event = models.ForeignKey(Eveniment, on_delete=models.CASCADE, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'

class Ticket(models.Model):
    TRIBUNA_CHOICES = [
        ('peluza_nord', 'Peluză Nord'),
        ('peluza_sud', 'Peluză Sud'),
        ('tribuna_1', 'Tribuna 1'),
        ('tribuna_2', 'Tribuna 2'),
    ]

    LOC_CHOICES = [(str(i), str(i)) for i in range(1, 5001)]

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

    tribuna = models.CharField(max_length=20, choices=TRIBUNA_CHOICES)
    numar_locuri = models.IntegerField(default=0)

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


class Stadion(models.Model):
    CAPACITY = 20000
    SECTOR_CHOICES = (
        ('peluza_nord', 'Peluză Nord'),
        ('peluza_sud', 'Peluză Sud'),
        ('tribuna_1', 'Tribuna 1'),
        ('tribuna_2', 'Tribuna 2'),
    )

    sector = models.CharField(max_length=20, choices=SECTOR_CHOICES)
    seat_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sector} - Locul {self.seat_number}"
