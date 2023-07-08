from django.shortcuts import render, redirect

from .forms import TicketForm, Stadion


# Create your views here.
def add_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            selected_seat = request.POST.get('seat')  # Obțineți locul selectat din cererea POST
            ticket.seat = selected_seat
            ticket.save()
            return redirect('home')  # Redirecționați la o altă pagină sau afișați un mesaj de succes
    else:
        form = TicketForm()
    return render(request, 'ticketing/register_ticket.html', {'form': form})





