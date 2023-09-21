from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    objects = CustomManager()

    def __str__(self):
        return self.email
