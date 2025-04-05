from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.core.exceptions import ValidationError
from .models import User, Fireman, IncidentCommander, Team

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

class CustomRegisterSerializer(RegisterSerializer):
    # Make username optional and allow it to be blank
    username = serializers.CharField(required=False, allow_blank=True, max_length=150)
    email = serializers.EmailField(required=True)
    
    def validate_email(self, email):
        """
        Validate that the email is unique.
        """
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email
    
    # Override validate_username to remove the uniqueness check from the base serializer
    def validate_username(self, username):
        # Since the model field is no longer unique, we don't need 
        # the base serializer's uniqueness check here. Return the value directly.
        return username
    
    def get_cleaned_data(self):
        # Call the superclass method first to get the base cleaned data
        data = super().get_cleaned_data()

        # Username generation logic is removed as username is no longer unique.
        # The `username` field definition still allows blank/missing usernames if desired.
        # Standard validation will still run for other fields.
        
        return data
    
    def custom_signup(self, request, user):
        # This method is called after the user is saved.
        pass # We don't need to do anything extra on signup

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class FiremanSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    team = TeamSerializer(many=True)

    class Meta:
        model = Fireman
        fields = "__all__"

class IncidentCommanderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    team = TeamSerializer(many=True)

    class Meta:
        model = IncidentCommander
        fields = "__all__"
