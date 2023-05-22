from django.db import models

from django.db import models
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import default


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=5)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.name


class Order(models.Model):  # comanda plasata de utilizator
    products = models.ManyToManyField(Product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):  # aceasta metoda returnează numele produsului și
        # este utilă pentru reprezentarea textuală
        return f"Order #{self.pk}"


class OrderItem(models.Model):  # inregistrare intre comanda si produsul din comanda
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()  # cantitatea produsului din comanda

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order #{self.order.pk})"
