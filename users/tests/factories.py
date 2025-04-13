import factory
import factory.fuzzy
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model

User = get_user_model()
ROLES = ["admin", "user"]


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    role = factory.fuzzy.FuzzyChoice(ROLES)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.LazyAttribute(
        lambda o: f"{o.first_name.lower()}.{o.last_name.lower()}@example.com"
    )
    phone_number = factory.Faker("phone_number")
