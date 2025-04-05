from main.lib.generic_api import GenericView
from .models import FiremanCoordinates, FiretruckCoordinates
from .serializers import FiremanCoordinatesSerializer, FiretruckCoordinatesSerializer
from rest_framework.permissions import IsAuthenticated

class FiremanCoordinatesView(GenericView):
    queryset = FiremanCoordinates.objects.all()
    serializer_class = FiremanCoordinatesSerializer
    permission_classes = [IsAuthenticated]
    cache_key_prefix = "fireman_coordinates"

class FiretruckCoordinatesView(GenericView):
    queryset = FiretruckCoordinates.objects.all()
    serializer_class = FiretruckCoordinatesSerializer
    permission_classes = [IsAuthenticated]
    cache_key_prefix = "firetruck_coordinates"
