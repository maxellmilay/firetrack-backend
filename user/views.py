from main.lib.generic_api import GenericView
from rest_framework.permissions import IsAuthenticated
from .models import User, Squad, Firestation
from .serializers import UserSerializer, SquadSerializer, FirestationSerializer

class UserView(GenericView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class SquadView(GenericView):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer
    permission_classes = [IsAuthenticated]
    
class FirestationView(GenericView):
    queryset = Firestation.objects.all()
    serializer_class = FirestationSerializer