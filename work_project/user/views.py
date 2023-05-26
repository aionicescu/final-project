from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

import user
from user.forms import UserForm
from user.models import User


class UserCreateView(CreateView):
    template_name = 'user/user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('list-of-user')
    permission_required = 'user.add_user'

    def get_queryset(self):
        return User.objects.filter(active=True)

    # def get_context_data(self, **kwargs):
    #     data = super().post(**kwargs)
    #     # now = datetime.datetime.now()
    #     # data['current_datetime'] = now
    #
    #     data['post_all_user'] = user

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return super().post(request, *args, **kwargs)
        return render(request, self.template_name, {"form": form})

    # get_context_data() = User.objects.filter(
    #     active=True)
    # filters = User(self.request.GET, queryset=get_context_data())
    #
    # get_context_data() = filters.qs
    #
    # data[
    #     'all_user'] = get_all_user
    # data[
    #     'form_filters'] = filters.form
    #
    # return data


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
    template_name = 'user/delete_user.html'
    model = User
    success_url = reverse_lazy('list-of-user')
    permission_required = 'user.delete_list_of_user'


class UserDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'user/details_user/html'
    model = User
    success_url = reverse_lazy('list-of-user')
    permission_required = 'user.details_list_of_user'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'user/update_user.html'
    model = User
    success_url = reverse_lazy('list-of-user')
    permission_required = 'user.update_list_of_user'


@login_required
def search(request):
    # accesam valoarea parametrului value pe care il gasim in url din browser la accesarea butonului search din formular
    get_value = request.GET.get('value')

    # icontains -> cautam stringul intr un alt string
    if get_value:
        get_data = User.objects.filter(Q(first_name__icontains=get_value) | Q(
            last_name__icontains=get_value))  # toti studentii care respecta conditia din filter
    else:
        get_data = User.objects.all()
    context = {'all_students': get_data}

    return render(request, 'User/search.html', context)
