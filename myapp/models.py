from django.db import models
from django.contrib.auth.models import AbstractUser

class Register(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=[
            ('Admin', 'Admin'),
            ('Officer', 'Officer'),
            ('Public', 'Public'),
        ],
        default='Public'
    )