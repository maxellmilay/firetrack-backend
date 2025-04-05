from django.db import models
from vehicle.models import Firetruck
from user.models import Fireman

class Incident(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    remarks = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class TravelOrder(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    firetruck = models.ForeignKey(Firetruck, on_delete=models.CASCADE)
    fireman = models.ManyToManyField(Fireman, related_name="travel_orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.incident.name} - {self.firetruck.name}"

class IncidentReport(models.Model):
    title = models.CharField(max_length=255)
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    report = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.incident.name}"
