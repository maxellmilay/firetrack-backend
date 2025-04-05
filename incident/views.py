from main.lib.generic_api import GenericView
from .models import Incident, TravelOrder, IncidentReport
from .serializers import IncidentSerializer, TravelOrderSerializer, IncidentReportSerializer
from rest_framework.permissions import IsAuthenticated

class IncidentView(GenericView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]
    cache_key_prefix = "incident"

class TravelOrderView(GenericView):
    queryset = TravelOrder.objects.all()
    serializer_class = TravelOrderSerializer
    permission_classes = [IsAuthenticated]
    cache_key_prefix = "travel_order"

class IncidentReportView(GenericView):
    queryset = IncidentReport.objects.all()
    serializer_class = IncidentReportSerializer
    permission_classes = [IsAuthenticated]
    cache_key_prefix = "incident_report"
