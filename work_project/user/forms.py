from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select

from user.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['first_name', 'last_name',
                  'age', 'email', 'description',
                  'active','gender']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'age': NumberInput(attrs={'placeholder': 'Please enter your age', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter your description', 'class': 'form-control',
                                           'rows': 3}),
            'gender': Select(attrs={'class': 'form-select'})
        }
