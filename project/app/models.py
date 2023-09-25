from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomManager

ROLES = (("A", "admin"),
         ("M", "manager"),
         ("E", "employee")
         )


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=20, choices=ROLES, default='E')
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'role']

    objects = CustomManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='mediafiles/images/')

    def __str__(self):
        return self.first_name
