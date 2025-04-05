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
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Fireman(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ManyToManyField(Team, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username

class IncidentCommander(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ManyToManyField(Team, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
