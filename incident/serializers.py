from rest_framework import serializers
from incident.models import Incident, IncidentReport
from user.models import User, Squad, Firestation
from user.serializers import UserSerializer

class IncidentSerializer(serializers.ModelSerializer):
    squad_ids = serializers.PrimaryKeyRelatedField(
        queryset=Squad.objects.all(),
        many=True,
        source='squads',
        write_only=True,
        required=False
    )
    squads = serializers.SerializerMethodField(read_only=True)
    creator_firestation = serializers.SerializerMethodField(read_only=True)

    def get_squads(self, obj):
        return [{
            'id': squad.id,
            'name': squad.name,
            'status': squad.status,
            'members': [{
                'id': member.id,
                'username': member.username,
                'role': member.role,
            } for member in squad.members.all()]
        } for squad in obj.squads.all()]

    def get_creator_firestation(self, obj):
        """Return the firestation of the incident creator."""
        if not obj.creator:
            return None
        firestations = obj.creator.firestations
        if firestations:
            fs = firestations[0]
            return {
                'id': fs.id,
                'name': fs.name,
            }
        return None

    class Meta:
        model = Incident
        fields = '__all__'

class IncidentReportSerializer(serializers.ModelSerializer):
    incident = IncidentSerializer(read_only=True)
    incident_id = serializers.PrimaryKeyRelatedField(queryset=Incident.objects.all(), source='incident')
    reporter = UserSerializer(read_only=True)
    reporter_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='reporter')
    class Meta:
        model = IncidentReport
        fields = '__all__'
