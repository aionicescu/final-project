from django.http import HttpResponse


def index(request):
    return HttpResponse('index.html')


def about(request):
    return HttpResponse('navbar.html')




