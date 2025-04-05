from main.lib.generic_api import GenericView
from .models import Firetruck
from .serializers import FiretruckSerializer
from rest_framework.permissions import IsAuthenticated

class FiretruckView(GenericView):
    queryset = Firetruck.objects.all()
    serializer_class = FiretruckSerializer
    permission_classes = [IsAuthenticated]
    cache_key_prefix = "firetruck"
