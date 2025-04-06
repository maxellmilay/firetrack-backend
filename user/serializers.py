from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.core.exceptions import ValidationError
from .models import User, Fireman, IncidentCommander, Team
from django.db import transaction

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
    # Use PrimaryKeyRelatedField for input, keep TeamSerializer for output (read_only=True)
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), many=True, write_only=True)
    team_details = TeamSerializer(many=True, read_only=True, source='team') # Separate field for read representation

    class Meta:
        model = Fireman
        # Adjust fields to include team_details for reading and exclude the write_only team field from default output
        fields = ['id', 'user', 'team', 'team_details', 'created_at', 'updated_at']
        read_only_fields = ['team_details'] # team_details is read-only

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        team_data = validated_data.pop('team')

        # Create the User instance
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        # Handle password hashing if password is provided
        password = user_data.get('password')
        user = user_serializer.save()
        if password:
            user.set_password(password)
            user.save()


        # Create the Fireman instance
        fireman = Fireman.objects.create(user=user, **validated_data)

        # Add teams to the Fireman instance
        if team_data:
            fireman.team.set(team_data)

        return fireman

class IncidentCommanderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # Use PrimaryKeyRelatedField for input, keep TeamSerializer for output (read_only=True)
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), many=True, write_only=True)
    team_details = TeamSerializer(many=True, read_only=True, source='team') # Separate field for read representation

    class Meta:
        model = IncidentCommander
        # Adjust fields to include team_details for reading and exclude the write_only team field from default output
        fields = ['id', 'user', 'team', 'team_details', 'created_at', 'updated_at']
        read_only_fields = ['team_details'] # team_details is read-only

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        team_data = validated_data.pop('team')

        # Create the User instance
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        # Handle password hashing if password is provided
        password = user_data.get('password')
        user = user_serializer.save()
        if password:
            user.set_password(password)
            user.save()

        # Create the IncidentCommander instance
        incident_commander = IncidentCommander.objects.create(user=user, **validated_data)

        # Add teams to the IncidentCommander instance
        if team_data:
            incident_commander.team.set(team_data)

        return incident_commander
