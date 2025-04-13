from django.db import models
class Coordinates(models.Model):
    tracker_id = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.tracker_id} - {self.latitude}, {self.longitude} - {self.timestamp}"
