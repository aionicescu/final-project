from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def homepage(request):
    context = {'segment': 'index'}
    return render(request, 'home/index.html', context)


