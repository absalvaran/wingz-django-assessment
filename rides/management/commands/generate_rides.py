from django.db import transaction
from django.core.management.base import BaseCommand

from rides.models import Ride, RideEvent
from rides.tests.factories import RideFactory, RideEventFactory


NUM_RIDES = 20


class Command(BaseCommand):
    help = "Generate test rides and ride events data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old rides and ride events data...")
        Ride.objects.all().delete()
        RideEvent.objects.all().delete()

        self.stdout.write("Creating new rides and ride events data...")
        for _ in range(NUM_RIDES):
            RideFactory()
            RideEventFactory()
