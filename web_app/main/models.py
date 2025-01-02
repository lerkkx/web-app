from django.db import models

class Registration(models.Model):
    username = models.CharField("username", max_length=50)
    email = models.CharField("email", max_length=100)
    password = models.CharField("password", max_length=50)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Registration"
        verbose_name_plural = "Registrations"

