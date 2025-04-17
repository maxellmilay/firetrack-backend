from main.lib.generic_api import GenericView
from map.models import Coordinates
from map.serializers import CoordinatesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class CoordinatesView(GenericView):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer

class LatestUserCoordinatesView(APIView):
    """
    API view to fetch the latest coordinates for a specific user
    """
    def get(self, request, tracker_id):
        try:
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
