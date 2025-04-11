from django.db import models

class Ride(models.Model):
    id_ride = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)
    id_rider = models.ForeignKey('User', on_delete=models.CASCADE)
    id_driver = models.ForeignKey('User', on_delete=models.CASCADE)
    pickup_latitude = models.FloatField()
    pickup_longitude = models.FloatField()
    dropoff_latitude = models.FloatField()
    dropoff_longitude = models.FloatField()
    pickup_time = models.DateTimeField()

    def __str__(self):
        return f"Ride {self.id_ride} - Status: {self.status}"
    

class RideEvent(models.Model):
    id_event = models.AutoField(primary_key=True)
    id_ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Event {self.id_event} - Type: {self.event_type}"

