from main.lib.generic_api import GenericView
from map.models import Coordinates
from map.serializers import CoordinatesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from user.models import User

class CoordinatesView(GenericView):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer
    permission_classes = [IsAuthenticated]
    
    def filter_queryset(self, filters, excludes):
        # Get base queryset with applied filters
        filter_q = Q(**filters)
        exclude_q = Q(**excludes)
        queryset = self.queryset.filter(filter_q).exclude(exclude_q)
        
        # Always filter by user's firestations
        # Get users in the same firestations as the current user
        users_in_same_firestations = User.objects.filter(
            squad__firestation__in=self.request.user.firestations
        ).distinct()
        
        # Get tracker_ids for these users
        tracker_ids = users_in_same_firestations.filter(
            tracker_id__isnull=False
        ).exclude(
            tracker_id=''
        ).values_list('tracker_id', flat=True)
        
        # Filter coordinates by these tracker_ids
        queryset = queryset.filter(tracker_id__in=tracker_ids)
            
        return queryset

class LatestUserCoordinatesView(APIView):
    """
    API view to fetch the latest coordinates for a specific user
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request, tracker_id):
        try:
            # Always check if the tracker_id belongs to a user in the same firestation
            user_firestations = request.user.firestations
            user_exists = User.objects.filter(
                tracker_id=tracker_id,
                squad__firestation__in=user_firestations
            ).exists()
            
            if not user_exists:
                return Response(
                    {"detail": "You don't have permission to view this user's location"},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            latest_coordinates = Coordinates.objects.filter(
                tracker_id=tracker_id
            ).order_by('-timestamp').first()
            
            if not latest_coordinates:
                return Response(
                    {"detail": f"No coordinates found for tracker ID: {tracker_id}"},
                    status=status.HTTP_404_NOT_FOUND
                )
                
            serializer = CoordinatesSerializer(latest_coordinates)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
