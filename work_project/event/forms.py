import form as form

from event.models import Eveniment
from ticketing import forms


class EventForm(forms.ModelForm):
    class Meta:
        model = Eveniment
        fields = ['title', 'user', 'status', 'description']



