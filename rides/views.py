from rest_framework import viewsets
from knox.auth import TokenAuthentication
from .models import Ride, RideEvent
from .serializers import RideSerializer, RideEventSerializer
from api.permissions import IsAdmin
from .filters import RideFilter


class RideViews(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdmin]
    serializer_class = RideSerializer
    filterset_class = RideFilter
    queryset = Ride.objects.all()


class RideEventViews(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdmin]
    serializer_class = RideEventSerializer
    queryset = RideEvent.objects.all()
