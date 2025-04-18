from django.db import models
from django.contrib.auth.models import AbstractUser

class Squad(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = 'AVAILABLE'
        UNAVAILABLE = 'UNAVAILABLE'
        
    name = models.CharField(max_length=255)
    leader = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True, related_name='led_squads')
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.AVAILABLE)
    firestation = models.ForeignKey('Firestation', on_delete=models.CASCADE, related_name='squads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    """Custom user model with additional fields."""
    
    class Role(models.TextChoices):
        ADMIN = 'ADMIN'
        FIREFIGHTER = 'FIREFIGHTER'
        TRUCK = 'TRUCK'

    username = models.CharField(max_length=255, unique=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    avatar_url = models.URLField(max_length=2000, blank=True, null=True)
    role = models.CharField(max_length=255, choices=Role.choices, default=Role.ADMIN)
    tracker_id = models.CharField(max_length=255, blank=True, null=True)
    squad = models.ManyToManyField(Squad, blank=True, related_name='members')

    def __str__(self):
        return self.email

    @property
    def firestations(self):
        """
        Returns a list of unique firestations associated with the user's squads.
        """
        return list(Firestation.objects.filter(squads__in=self.squad.all()).distinct())

class Firestation(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
