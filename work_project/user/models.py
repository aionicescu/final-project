from django.db import models
from django.http import HttpResponse


class User(models.Model):
    gender_options = (('male', 'Male'), ('female', 'Female'))

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=30)
    description = models.TextField(max_length=300)
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    gender = models.CharField(max_length=6, choices=gender_options)

    created_at = models.DateTimeField(auto_now_add=True,
                                      null=True)
    updated_at = models.DateTimeField(auto_now=True,
                                      null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.qs = None
        self.form = None

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
