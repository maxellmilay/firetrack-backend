from django.db import models
from user.models import Fireman
from vehicle.models import Firetruck

class FiremanCoordinates(models.Model):
    fireman = models.ForeignKey(Fireman, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.fireman.name} - {self.timestamp}"
    
class FiretruckCoordinates(models.Model):
    truck = models.ForeignKey(Firetruck, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.truck.name} - {self.timestamp}"
