from main.lib.generic_api import GenericView
from incident.models import Incident, IncidentReport
from incident.serializers import IncidentSerializer, IncidentReportSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class IncidentView(GenericView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]
    
    def filter_queryset(self, filters, excludes):
        # Get base queryset with applied filters
        filter_q = Q(**filters)
        exclude_q = Q(**excludes)
        queryset = self.queryset.filter(filter_q).exclude(exclude_q)
        
        # Always filter by user's firestations
        # Filter incidents by creator's firestation
        queryset = queryset.filter(
            creator__squad__firestation__in=self.request.user.firestations
        ).distinct()
            
        return queryset

class AllIncidentsView(GenericView):
    """Returns all incidents without user-based filtering (for map display)."""
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]


class IncidentReportView(GenericView):
    queryset = IncidentReport.objects.all()
    serializer_class = IncidentReportSerializer
    permission_classes = [IsAuthenticated]
    
    def filter_queryset(self, filters, excludes):
        # Get base queryset with applied filters
        filter_q = Q(**filters)
        exclude_q = Q(**excludes)
        queryset = self.queryset.filter(filter_q).exclude(exclude_q)
        
        # Always filter by user's firestations
        # Filter reports for incidents related to the user's firestation
        queryset = queryset.filter(
            Q(incident__creator__squad__firestation__in=self.request.user.firestations) |
            Q(reporter__squad__firestation__in=self.request.user.firestations)
        ).distinct()
            
        return queryset
