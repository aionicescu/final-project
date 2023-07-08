from tkinter import Place

import cart as cart
from django.http import request

from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView

from .models import Product, Order, OrderItem


class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    # def get(self, request):
    #     products = Product.objects.all()
    #     return render(request, 'shop/product_list.html', {'products': products})


class PlaceOrderView(View):
    model = Place
    template_name = 'shop/order_success.html'
    # def get(self, request):
    #     cart = Cart.objects.get(user=request.user)
    #     return render(request, 'shop/order_success.html', {'cart': cart})


class OrderSuccessView(View):
    model = Order
    template_name = 'shop/order_success.html'