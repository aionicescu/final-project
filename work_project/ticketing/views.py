from django.shortcuts import render, redirect

from .forms import TicketForm


# Create your views here.
def add_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TicketForm()
        return render(request, 'ticketing/register_ticket.html', {'form': form})
