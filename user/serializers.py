from rest_framework import serializers
from .models import User, Squad, Firestation
from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer

class LoginSerializer(RestAuthLoginSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    
class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    date_joined = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    class Meta:
        model = User
        exclude = ['password', 'groups', 'user_permissions', 'first_name', 'last_name']

class FirestationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firestation
        fields = "__all__"

class SquadSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    firestation = FirestationSerializer(read_only=True)
    firestation_id = serializers.PrimaryKeyRelatedField(queryset=Firestation.objects.all(), source='firestation')
    leader = UserSerializer(read_only=True)
    leader_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='leader')
    class Meta:
        model = Squad
        fields = "__all__"
