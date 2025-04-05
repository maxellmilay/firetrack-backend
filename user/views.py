from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Fireman, IncidentCommander, Team
from .serializers import FiremanSerializer, IncidentCommanderSerializer, TeamSerializer

class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]
    cache_key_prefix = "team"

class FiremanView(viewsets.ModelViewSet):
    queryset = Fireman.objects.all()
    serializer_class = FiremanSerializer
    permission_classes = [IsAuthenticated]
    cache_key_prefix = "fireman"
class IncidentCommanderView(viewsets.ModelViewSet):
    queryset = IncidentCommander.objects.all()
    serializer_class = IncidentCommanderSerializer
    permission_classes = [IsAuthenticated]
    cache_key_prefix = "incident_commander"
