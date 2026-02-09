from main.lib.generic_api import GenericView
from rest_framework.permissions import IsAuthenticated
from .models import User, Squad, Firestation
from .serializers import UserSerializer, SquadSerializer, FirestationSerializer
from django.db.models import Q

class UserView(GenericView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def filter_queryset(self, filters, excludes):
        # Get base queryset with applied filters
        filter_q = Q(**filters)
        exclude_q = Q(**excludes)
        queryset = self.queryset.filter(filter_q).exclude(exclude_q)
        
        # Always filter by user's firestations
        user_firestations = self.request.user.firestations
        # Find users that belong to the same firestations
        users_with_matching_firestations = User.objects.filter(
            squad__firestation__in=user_firestations
        ).distinct()
        queryset = queryset.filter(id__in=users_with_matching_firestations)
            
        return queryset

class SquadView(GenericView):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer
    
    def filter_queryset(self, filters, excludes):
        # Get base queryset with applied filters
        filter_q = Q(**filters)
        exclude_q = Q(**excludes)
        queryset = self.queryset.filter(filter_q).exclude(exclude_q)
        
        # Always filter by user's firestations
        user_firestations = self.request.user.firestations
        queryset = queryset.filter(firestation__in=user_firestations)
            
        return queryset
    
class FirestationView(GenericView):
    queryset = Firestation.objects.all()
    serializer_class = FirestationSerializer
    
    def filter_queryset(self, filters, excludes):
        # Get base queryset with applied filters
        filter_q = Q(**filters)
        exclude_q = Q(**excludes)
        queryset = self.queryset.filter(filter_q).exclude(exclude_q)
        
        # Always filter by user's firestations
        user_firestations = self.request.user.firestations
        queryset = queryset.filter(id__in=[fs.id for fs in user_firestations])
            
        return queryset


class AllFirestationsView(GenericView):
    """Returns all fire stations without user-based filtering (for map display)."""
    queryset = Firestation.objects.all()
    serializer_class = FirestationSerializer