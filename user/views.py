import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from django.contrib.auth.decorators import login_required

from user.filters import UserFilter
from user.forms import UserForm
from user.models import User


class UserCreateView(CreateView):
    template_name = 'user/user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy(
        'list-of-users') # de trecut redirectionarea catre un mesaj de bun venit
    permission_required = 'user.add_user'

class UserListView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    template_name = 'user/list_of_user.html'
    model = User
    context_object_name = 'all_user'
    permission_required = 'user.add_user'

    def get_queryset(self):
        return User.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        now = datetime.datetime.now()
        data['current_datetime'] = now
        get_all_users = User.objects.filter(
            active=True)  # stochez intr-o variabila toti userii care sunt active=True(vezi querydin def get_queryset
        filters = UserFilter(self.request.GET,
                                queryset=get_all_users)  # in functie de ce introduce utilizatroul in formularul de filtrare vom cauta prin query stocat in get_all_students
        get_all_users = filters.qs  # dupa realizarea filtrarii vor ramane stundeti ce vor respecta criteriile date de utilizator in fomrularul de filtrares

        data[
            'all_users'] = get_all_users  # reinitializez cheia all_users din dictionarul data cu datele ce vin din urma filtrarii
        data[
            'form_filters'] = filters.form  # trimit in pagina list_of_users.html formualrul de filtrare prin cheia form_filters


        return data

class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'registration/delete_user.html'
    model = User
    success_url = reverse_lazy('list-of-users')
    permission_required = 'user.delete_list_of_users'


class UserDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'registration/details_user.html'
    model = User


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/update_user.html'
    model = User
    success_url = reverse_lazy('list-of-users')
    permission_required = 'user.update_list_of_users'


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

@permission_required('user.inactive_user')
def deactivate_student(request, pk):
    User.objects.filter(id=pk).update(active=False)

    return redirect('list-of-users')



