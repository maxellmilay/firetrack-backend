from django.db import models
from django.contrib.auth.models import AbstractUser

class Squad(models.Model):
    name = models.CharField(max_length=255)
    leader = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True, related_name='led_squads')
    description = models.TextField(blank=True, null=True)
    firestation = models.ForeignKey('Firestation', on_delete=models.CASCADE, related_name='squads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    """Custom user model with additional fields."""
    
    class Role(models.TextChoices):
        ADMIN = 'ADMIN'
        FIREFIREFIGHTER = 'FIREFIREFIGHTER'
        TRUCK = 'TRUCK'

    username = models.CharField(max_length=255, unique=True)
    avatar_url = models.URLField(max_length=2000, blank=True, null=True)
    role = models.CharField(max_length=255, choices=Role.choices)
    tracker_id = models.CharField(max_length=255, blank=True, null=True)
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE, blank=True, null=True, related_name='members')

    def __str__(self):
        return self.email

class Firestation(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
