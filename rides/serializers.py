from django.utils.timezone import now, timedelta
from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Ride, RideEvent


class RideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = "__all__"


class RideSerializer(serializers.ModelSerializer):
    serializers.ListField(source="todays_ride_events", child=serializers.IntegerField())
    distance_to_pickup = serializers.SerializerMethodField()

    class Meta:
        model = Ride
        fields = "__all__"

    # Uncomment if RideEvents need to be serialized
    # def get_todays_ride_events(self, obj):
    # one_day_ago = now() - timedelta(days=1)
    # events = obj.events.filter(created_at__gte=one_day_ago)
    # # return RideEventSerializer(events, many=True).data
    # return events.values_list("id_event", flat=True)

    def get_distance_to_pickup(self, obj):
        return getattr(obj, "distance_to_pickup", None)
