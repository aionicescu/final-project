from django.urls import path

from user import views

urlpatterns = [

    path('list/', views.UserListView.as_view(), name='list-of-user', )

]