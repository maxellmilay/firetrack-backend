from django.db import models
from user.models import User

class Incident(models.Model):
    class Status(models.TextChoices):
        IN_PROGRESS = 'IN PROGRESS'
        ENDED = 'ENDED'

    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    response_time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=Status.choices)
    remarks = models.TextField(null=True, blank=True)
    location_name = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_ended = models.DateTimeField(null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class IncidentReport(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    file = models.URLField(max_length=2000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
