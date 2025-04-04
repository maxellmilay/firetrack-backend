from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Custom user model with additional fields."""

    username = models.CharField(max_length=30, null=True, blank=True, unique=False)
    email = models.EmailField(unique=True)
    image_url = models.URLField(max_length=2000, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email
