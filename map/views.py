from main.lib.generic_api import GenericView
from map.models import Coordinates
from map.serializers import CoordinatesSerializer

class CoordinatesView(GenericView):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer
