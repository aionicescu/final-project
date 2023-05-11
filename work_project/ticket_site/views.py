from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse('base.html')


def about(request):
    return HttpResponse('navbar.html')



def base(request):
  template = loader.get_template('base.html')
  return HttpResponse(template.render())

# commit
