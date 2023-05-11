

from django.shortcuts import render

# Create your views here.

def homepage(request):
    context = {'segment': 'index'}
    return render(request, 'home/index.html', context)
