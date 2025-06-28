from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(
        max_length=150,
        unique=True
    )
