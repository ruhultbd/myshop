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

    def __str__(self):
        return self.name


class Product(models.Model):
    class StatusOptions(models.TextChoices):
        Active = 'active'
        Inactive = 'inactive'

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    short_desc = models.TextField(null=True)
    long_desc = models.TextField(null=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    sku = models.CharField(max_length=128)
    status = models.CharField(max_length=10, choices=StatusOptions.choices, default=StatusOptions.Active)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
