from rest_framework import serializers
from .models import User, Squad, Firestation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class SquadSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    class Meta:
        model = Squad
        fields = "__all__"

class FirestationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firestation
        fields = "__all__"
