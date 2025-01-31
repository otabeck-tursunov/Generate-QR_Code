from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=13)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username


