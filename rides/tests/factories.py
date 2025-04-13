import factory
import factory.fuzzy
from factory.django import DjangoModelFactory
from faker import Faker
from django.utils import timezone

from rides.models import Ride, RideEvent
from users.tests.factories import UserFactory


fake = Faker()
STATUS = ["ENROUTE", "PICKUP", "DROPOFF"]


class RideFactory(DjangoModelFactory):
    class Meta:
        model = Ride

    status = factory.fuzzy.FuzzyChoice(STATUS)
    id_rider = factory.SubFactory(UserFactory)
    id_driver = factory.SubFactory(UserFactory)
    pickup_latitude = factory.LazyFunction(lambda: fake.latitude())
    pickup_longitude = factory.LazyFunction(lambda: fake.longitude())
    dropoff_latitude = factory.LazyFunction(lambda: fake.latitude())
    dropoff_longitude = factory.LazyFunction(lambda: fake.longitude())
    pickup_time = factory.Faker(
        "date_time_this_year", tzinfo=timezone.get_current_timezone()
    )


class RideEventFactory(DjangoModelFactory):
    class Meta:
        model = RideEvent

    id_ride = factory.SubFactory(RideFactory)
    description = factory.Faker("paragraph")
    created_at = factory.Faker(
        "date_time_this_year", tzinfo=timezone.get_current_timezone()
    )
