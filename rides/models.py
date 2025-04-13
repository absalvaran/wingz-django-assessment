from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Ride(models.Model):
    STATUS_CHOICES = (
        ("enroute", "en-route"),
        ("pickup", "pickup"),
        ("dropoff", "dropoff"),
    )

    id_ride = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="ENROUTE")
    id_rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rider")
    id_driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="driver")
    pickup_latitude = models.FloatField()
    pickup_longitude = models.FloatField()
    dropoff_latitude = models.FloatField()
    dropoff_longitude = models.FloatField()
    pickup_time = models.DateTimeField()

    def __str__(self):
        return f"Ride {self.id_ride} - Status: {self.status}"


class RideEvent(models.Model):
    id_event = models.AutoField(primary_key=True)
    id_ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name="events")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Event {self.id_event} - Ride: {self.id_ride}"
