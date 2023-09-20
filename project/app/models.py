from django.db import models


class SignUp(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    objects = models.Manager()

    def __str__(self):
        return self.username


class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    objects = models.Manager()

    def __str__(self):
        return self.username

