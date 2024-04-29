from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=10)
    introduction = models.TextField(blank=True)

    def __str__(self):
        return self.username
