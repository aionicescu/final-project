
from django.forms import TextInput, EmailInput, Textarea, DateInput, Select, forms


class TicketForm(forms.ModelForm):
    class Meta:

        fields = ['first_name', 'last_name',
                  'email', 'description', 'active', 'start_date',
                  'end_date', 'event']
    widgets = {
        'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
        'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
        'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
        'description': Textarea(attrs={'placeholder': 'Please enter your description', 'class': 'form-control',
                                       'rows': 3}),
        'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'event': Select(attrs={'class': 'form-select'})
    }





