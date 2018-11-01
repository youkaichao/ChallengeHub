from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(blank=False)
    introduction = models.TextField(default='')
    school = models.CharField(default='', max_length=64)
    individual = models.BooleanField()
