from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from ticket_site.models import Order


def index(request):
    return HttpResponse('base.html')


def about(request):
    return HttpResponse('navbar.html')


def base(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


# commit

def informatii_view(request):
    return render(request, 'informatii.html')


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})
