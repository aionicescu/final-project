from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from jinja2.ext import do
from django.contrib.auth.decorators import login_required
import user
from user.forms import UserForm
from user.models import User
import datetime


class UserCreateView(CreateView):
    template_name = 'user/user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('list-of-user')
    permission_required = 'user.add_user'

    def get_queryset(self):
        return User.objects.filter(active=True)

    # def get_context_data(self, **kwargs):
    #     login_required()
    #     data = super().get_context_data(**kwargs)
    #     now = datetime.datetime.now()
    #     data['current_datetime'] = now
    #     trainers = User.objects.all()
    #     data['get_all_user'] = User
    #
    #     get_all_students = User.objects.filter(
    #         active=True)
    #     filters = User(self.request.GET,
    #                    queryset=get_all_students)
    #     get_all_user = filters.qs
    #
    #     data[
    #         'all_user'] = get_all_user
    #     data[
    #         'form_filters'] = filters.form
    #
    #     return data

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return super().post(request, *args, **kwargs)
        return render(request, self.template_name, {"form": form})


class UserListView(ListView):
    template_name = 'user/list_of_user.html'
    model = User
    context_object_name = 'all_user'
    form_class = UserForm
    success_url = reverse_lazy('list-of-user')
    permission_required = 'user.add_user'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return super().post(request, *args, **kwargs)
        return render(request, self.template_name, {"form": form})

    # permission_required = 'user.view_list_of_user'


def informatii_view(request):
    return True


class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'registration/delete_user.html'
    model = User
    success_url = reverse_lazy('list-of-user')
    permission_required = 'user.delete_list_of_user'


class UserDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'registration/details_user.html'
    model = User
    success_url = reverse_lazy('list-of-user')
    permission_required = 'user.details_list_of_user'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/update_user.html'
    model = User
    success_url = reverse_lazy('list-of-user')
    permission_required = 'user.update_list_of_user'


@login_required(login_url="html page")
def search(request):
    get_value = request.GET.get('value')

    if get_value:
        get_data = User.objects.filter(Q(first_name__icontains=get_value) | Q(
            last_name__icontains=get_value))
    else:
        get_data = User.objects.all()
    context = {'all_user': get_data}

    return render(request, 'registration/search.html', context)


