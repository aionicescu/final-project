
from django.forms import TextInput, EmailInput, Textarea, DateInput, Select
from django.forms import ModelForm

from ticketing.models import Ticket
from ticketing.models import Stadion
from django import forms


# class TicketForm(ModelForm):
#
#     class Meta:
#         model=Ticket
#         fields = "__all__"
    # widgets = {
    #     'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
    #     'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
    #     'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
    #     'description': Textarea(attrs={'placeholder': 'Please enter your description', 'class': 'form-control',
    #                                    'rows': 3}),
    #     'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    #     'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    #     'event': Select(attrs={'class': 'form-select'})
    # }

class TicketForm(forms.ModelForm):
    seat = forms.ChoiceField(choices=[('peluza_nord', 'Peluză Nord'), ('peluza_sud', 'Peluză Sud'), ('tribuna_1', 'Tribuna 1'), ('tribuna_2', 'Tribuna 2')])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # occupied_seats = Ticket.objects.values_list('event__tribuna', flat=True)  # Locurile deja ocupate
        # available_seats = [str(i) for i in range(1, 20001) if str(i) not in occupied_seats]  # Locurile disponibile
        # self.fields['seat'].choices = [(seat, seat) for seat in available_seats]

    class Meta:
        model = Ticket
        fields = "__all__"






