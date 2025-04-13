from main.lib.generic_api import GenericView
from incident.models import Incident, IncidentReport
from incident.serializers import IncidentSerializer, IncidentReportSerializer
from rest_framework.permissions import IsAuthenticated

class IncidentView(GenericView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]

class IncidentReportView(GenericView):
    queryset = IncidentReport.objects.all()
    serializer_class = IncidentReportSerializer
    permission_classes = [IsAuthenticated]
