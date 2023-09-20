from django.db import models
from django.contrib.auth.hashers import make_password


class CustomUser(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
