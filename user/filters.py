import django_filters
from django import forms
from django_filters import DateFilter


# Definim o clasa in care specificam modelul si fieldurile ce apartin modelului pe care le vom avea in FORMULARUL DE FILTRARE

# lookup_expr -> icontains, startswith, endswith, exact, lte, lt, gte, gt

# gte -> greater than or equal to
# gt -> greater than

# lte -> less than or egual to
# lt ->  less than
from user.models import User


class UserFilter(django_filters.FilterSet):

    #list_of_user = [(user.first_name, user.first_name.upper()) for user in User.objects.all() if user.active is True]


    # pentru a elimina datele duplicate dintr-o lista il vom converti intr-un set si pt pastrarea ordinii elem din set convert in lista
    #first_name = django_filters.ChoiceFilter(choices=list(set(list_of_user)))
    first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name')
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name')


    start_date_gte = DateFilter(field_name='start_date', lookup_expr='gte', label='From start date',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    start_date_lte = DateFilter(field_name='start_date', lookup_expr='lte', label='To start date',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'active', 'start_date_gte', 'start_date_lte']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # daca se merge cu varianta CharFilter se va adauga si placeholderul-> , 'placeholder': 'Please enter first_name' si class -> 'class': 'form-control'
        #self.filters['first_name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter first name'})

        # daca merg cu varianta de ChoiceFilter
        self.filters['first_name'].field.widget.attrs.update({'class': 'form-select'})
        self.filters['last_name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter last name'})
        self.filters['active'].field.widget.attrs.update({'class': 'form-select'})