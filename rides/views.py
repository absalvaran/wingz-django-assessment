from rest_framework import viewsets
from knox.auth import TokenAuthentication
from .models import Ride, RideEvent
from .serializers import RideSerializer, RideEventSerializer


class RideViews(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = RideSerializer
    queryset = Ride.objects.all()


class RideEventViews(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = RideEventSerializer
    queryset = RideEvent.objects.all()
