from django.core.management.base import BaseCommand
from django.db import transaction

from users.models import User
from users.tests.factories import UserFactory

NUM_USERS = 3


class Command(BaseCommand):
    help = "Generates test user data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old user data...")
        User.objects.all().delete()

        self.stdout.write("Creating new user data...")
        for _ in range(NUM_USERS):
            UserFactory()
