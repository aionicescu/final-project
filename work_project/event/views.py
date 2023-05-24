from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Eveniment


def user_events(request):
    if request.user.id:
        events = Eveniment.objects.filter(user_id=request.user.id).all()
        return render(request, 'event/evenimente.html', {'events': events})
    else:
        events = Eveniment.objects.all()
        context = {'events': events}
        return render(request, 'event/evenimente.html', context)



# def create_event(request):
#     if request.method == 'POST':
#         form = EventForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('event:event_list')
#     else:
#         form = EventForm()
#     return render(request, 'event/evenimente.html', {'form': form})


from django.contrib.auth.decorators import login_required
from event.models import Eveniment
from ticketing import forms

@login_required
def create_event(request):
    if request.method == 'post':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('event:event_list')
    else:
        form = EventForm()
    return render(request, 'event/evenimente.html', {'form': form})
