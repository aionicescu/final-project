from django.urls import path
from .views import  user_events, create_event

urlpatterns = [
    path('', user_events, name='event_list'),
    path('create/', create_event, name='create_event')
]

