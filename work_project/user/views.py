from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

import user
from user.forms import UserForm
from user.models import User


class UserCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'user/user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('list-of-user')
    permission_required = 'user.add_user'

    def get_queryset(self):
        return User.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # now = datetime.datetime.now()
        # data['current_datetime'] = now

        data['get_all_user'] = user
        get_all_user = User.objects.filter(
            active=True)
        filters = User(self.request.GET, queryset=get_all_user)

        get_all_user = filters.qs

        data[
            'all_students'] = get_all_user
        data[
            'form_filters'] = filters.form

        return data


class UserListView(ListView):
    template_name = 'user/list_of_user.html'
    model = User
    context_object_name = 'all_user'
    # permission_required = 'user.view_list_of_user'
