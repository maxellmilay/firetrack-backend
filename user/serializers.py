from rest_framework import serializers
from .models import User, Squad, Firestation
from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer as RestAuthRegisterSerializer

class LoginSerializer(RestAuthLoginSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    
class RegisterSerializer(RestAuthRegisterSerializer):
    role = serializers.ChoiceField(choices=User.Role.choices, default=User.Role.ADMIN)
    display_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    avatar_url = serializers.URLField(required=False, allow_blank=True, allow_null=True)
    tracker_id = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    
    def custom_signup(self, request, user):
        user.role = self.validated_data.get('role', User.Role.ADMIN)
        user.display_name = self.validated_data.get('display_name', '')
        user.avatar_url = self.validated_data.get('avatar_url', '')
        user.tracker_id = self.validated_data.get('tracker_id', '')
        user.save()
    
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
