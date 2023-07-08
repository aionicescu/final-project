from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.http import HttpResponse

class User(AbstractBaseUser):
    gender_options = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    age = models.IntegerField()
    description = models.TextField(max_length=300)
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    gender = models.CharField(max_length=6, choices=gender_options)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# class User(models.Model):
#     gender_options = (('male', 'Male'), ('female', 'Female'))
#
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     age = models.IntegerField()
#     email = models.EmailField(max_length=30)
#     description = models.TextField(max_length=300)
#     active = models.BooleanField(default=True)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     gender = models.CharField(max_length=6, choices=gender_options)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#
# class Category(models.Model):
#     category_name = models.CharField(max_length=50, null=True)
#
#     class Meta:
#         db_table = 'my_category_table'
#
#
# def __str__(self):
#     return f'{self.first_name} {self.last_name}'

