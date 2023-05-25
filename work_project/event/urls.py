from django.urls import path

from event.views import create_event, user_events, adauga_eveniment

urlpatterns = [
    path('user/', user_events, name='event_list'),
    path('create/', create_event, name='create_event'),
    path('event/', create_event, name='adauga_eveniment'),
    path('event/', adauga_eveniment, name='adauga_eveniment')
]

