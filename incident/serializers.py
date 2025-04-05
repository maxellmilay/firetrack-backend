from rest_framework import serializers
from .models import Incident, TravelOrder, IncidentReport
from vehicle.serializers import FiretruckSerializer
from user.serializers import FiremanSerializer

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'
        
class TravelOrderSerializer(serializers.ModelSerializer):
    firetruck = FiretruckSerializer()
    fireman = FiremanSerializer(many=True)
    incident = IncidentSerializer()
    
    class Meta:
        model = TravelOrder
        fields = '__all__'
        
class IncidentReportSerializer(serializers.ModelSerializer):
    incident = IncidentSerializer()
    
    class Meta:
        model = IncidentReport
        fields = '__all__'
