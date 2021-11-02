from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    class StatusOptions(models.TextChoices):
        Active = 'Active'
        Inactive = 'Inactive'

    name = models.CharField(max_length=128)
    parent = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=StatusOptions.choices, default=StatusOptions.Active)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
