from django.db import connection
from django.db.models import ExpressionWrapper, F, FloatField, Prefetch
from django.db.models.functions import Power, Sqrt
from django.utils.timezone import now, timedelta
from knox.auth import TokenAuthentication
from rest_framework import viewsets

from api.permissions import IsAdmin

from .filters import RideFilter
from .models import Ride, RideEvent
from .serializers import RideEventSerializer, RideSerializer


class RideView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdmin]
    serializer_class = RideSerializer
    filterset_class = RideFilter
    ordering_fields = ["pickup_time"]
    ordering = ["pickup_time"]

    def get_queryset(self):
        within_24_hours = now() - timedelta(hours=24)
        queryset = Ride.objects.select_related(
            "id_rider", "id_driver"
        ).prefetch_related(
            Prefetch(
                "events",
                queryset=RideEvent.objects.filter(created_at__gte=within_24_hours),
                to_attr="todays_ride_events",
            )
        )
        latitude = self.request.query_params.get("latitude")
        longitude = self.request.query_params.get("longitude")
        if latitude and longitude:
            try:
                latitude = float(latitude)
                longitude = float(longitude)
                queryset = queryset.annotate(
                    distance_to_pickup=ExpressionWrapper(
                        Sqrt(
                            Power(F("pickup_latitude") - latitude, 2)
                            + Power(F("pickup_longitude") - longitude, 2)
                        ),
                        output_field=FloatField(),
                    )
                )
            except ValueError:
                # Return queryset without annotation if lat/lng is invalid (i.e. letters, symbols)
                pass
        return queryset


class RideEventView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdmin]
    serializer_class = RideEventSerializer
