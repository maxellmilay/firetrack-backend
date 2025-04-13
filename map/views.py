from main.lib.generic_api import GenericView
from map.models import Coordinates
from map.serializers import CoordinatesSerializer
from rest_framework.permissions import IsAuthenticated

class CoordinatesView(GenericView):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer
    permission_classes = [IsAuthenticated]
