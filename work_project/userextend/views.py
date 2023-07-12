from django.conf.global_settings import EMAIL_HOST_USER
from django.shortcuts import render

# Create your views here.
from random import random

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

import home
from user.forms import UserForm

class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm

    # success_url = revehrse_lazy('homepage')#DACA FOLOSESC DEF FOR_VALID(self,form) NU am nevoie de

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            new_user.username = f"{new_user.first_name.lower()}{new_user.last_name.lower()}_{random.randint(100000, 999999)}"
            new_user.save()

            # TRIMIT MAIL FARA TEMPLATE

            subject = 'Felicitari! Ai un cont nou in aplicatie!'
            message = f'Hello, {new_user.first_name} {new_user.last_name}. Usernameul tau este {new_user.username}'
            send_mail(subject, message, EMAIL_HOST_USER, [new_user.email])

            # TRIMIT   mail cu template

            details = {
                'fullname': f'{new_user.first_name} {new_user.last_name}',
                'username': new_user.username
            }
            subject = 'Felicitari! Ai un cont nou in aplicatie! '
            message = get_template('userextend/mail.html').render(details)
            mail = EmailMessage(
                subject,
                message,
                EMAIL_HOST_USER,
                [new_user.email]
            )
            mail.content_subtype = 'html'
            mail.send()

        return redirect('login')
