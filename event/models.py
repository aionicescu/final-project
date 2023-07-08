from django.db import models

from user.models import User

CHOICES = [(1,'To Do'), (2,'In Progress'), (3,'In Review'), (4,'Done')]


class Eveniment(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=CHOICES, default=CHOICES[0])
    description = models.TextField()
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
