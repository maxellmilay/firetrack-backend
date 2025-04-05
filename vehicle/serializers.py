from rest_framework import serializers
from .models import Firetruck

class FiretruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firetruck
        fields = '__all__'
