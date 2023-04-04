from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.backends import django

# var = django.db.models.BigAutoField


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
