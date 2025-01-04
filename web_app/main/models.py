from django.db import models
from django.contrib.auth.models import AbstractUser

class UserRegistration(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username



    # новое
    last_login = models.DateTimeField(null=True, blank=True)
    REQUIRED_FIELDS = ['USERNAME_FIELD','EMAIL_FIELD', 'PASSWORD_FIELD']