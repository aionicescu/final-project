from django.urls import path

from .views import UserCreateView, UserListView, UserUpdateView, UserDeleteView, UserDetailsView, search

urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='create-user'),
    path('list_of_users/', UserListView.as_view(), name='list-of-users'),
    path('update_user/<int:pk>/', UserUpdateView.as_view(), name='update-user'),
    path('delete_user/<int:pk>/', UserDeleteView.as_view(), name='delete-user'),
    path('details_user/<int:pk>/', UserDetailsView.as_view(), name='details-user'),
    path('search/', search, name='search'),
]
