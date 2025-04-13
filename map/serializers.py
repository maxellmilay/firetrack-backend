from rest_framework import serializers
from map.models import Coordinates

class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = '__all__'

