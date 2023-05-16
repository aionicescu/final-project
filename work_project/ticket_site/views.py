from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from ticket_site.forms import TicketForm
from ticket_site.models import Order, Ticket


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


def register_ticket(request):
    # if request.method == 'POST':
    #     form = TicketForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    # else:
    form = TicketForm()
    #
    context = {'form': form}

    return render(request, 'ticket_site/register_ticket.html', context)

# class TicketDetailView(View):
#     def get(self, request, ticket_id):
#         ticket = Ticket.objects.get(id=ticket_id)
#         return render(request, 'ticket_detail.html', {'ticket': ticket})
