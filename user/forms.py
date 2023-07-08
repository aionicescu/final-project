from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select
from user.models import User


class UserForm(UserCreationForm):
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User

        fields = ['email', 'phone_number', 'age', 'description', 'active', 'start_date', 'end_date', 'gender']

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'phone_number': forms.TextInput(
                attrs={'placeholder': 'Please enter your phone number', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Please enter your age', 'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Please enter your description', 'class': 'form-control', 'rows': 3}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        get_email = cleaned_data['email']
        check_emails = User.objects.filter(
            email=get_email)
        if check_emails:
            msg = 'Email already exists in database'
            self._errors['email'] = self.error_class([msg])

        get_start_date = cleaned_data['start_date']
        get_end_date = cleaned_data['end_date']

        if get_start_date > get_end_date:
            msg = ' Start date is greater than end date'
            self._errors['start_date'] = self.error_class([msg])

        return cleaned_data


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['age', 'email', 'description', 'active', 'start_date', 'end_date', 'gender']

        widgets = {
            'age': forms.NumberInput(attrs={'placeholder': 'Please enter your age', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Please enter your description', 'class': 'form-control', 'rows': 3}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
        }
