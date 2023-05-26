from django.urls import path

from user import views

urlpatterns = [

    path('list/', views.UserListView.as_view(), name='list-of-user', ),
    path('create/', views.UserCreateView.as_view(), name='create-user', ),
    path('delete_user/,<int:pk>/', views.UserDeleteView.as_view(), name='delete-user'),
    path('details_user/,<int:pk>/', views.UserDetailsView.as_view(), name='details-user'),
    path('update_user/,<int:pk>/', views.UserUpdateView.as_view(), name='update-user'),
    path('search/', views.search, name='search'),

]
