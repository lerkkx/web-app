
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class UserRegistration(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    token_timestamp = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    # новое
    last_login = models.DateTimeField(null=True, blank=True)