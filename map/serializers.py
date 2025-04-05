from rest_framework import serializers
from .models import FiremanCoordinates, FiretruckCoordinates
from user.serializers import FiremanSerializer
from vehicle.serializers import FiretruckSerializer

class FiremanCoordinatesSerializer(serializers.ModelSerializer):
    fireman = FiremanSerializer()
    
    class Meta:
        model = FiremanCoordinates
        fields = '__all__'

class FiretruckCoordinatesSerializer(serializers.ModelSerializer):
    truck = FiretruckSerializer()
    
    class Meta:
        model = FiretruckCoordinates
        fields = '__all__'
