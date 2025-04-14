from rest_framework import serializers
from incident.models import Incident, IncidentReport
from user.models import User
from user.serializers import UserSerializer
class IncidentSerializer(serializers.ModelSerializer):
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
