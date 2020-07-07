import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations.models import Reservation
from users import models as users_model
from rooms import models as rooms_model

NAME = "Reservations"


class Command(BaseCommand):

    help = 'This command create {NAME}"'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many {NAME} do you want create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        all_users = users_model.User.objects.all()
        all_rooms = rooms_model.Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "guest": lambda x: random.choice(all_users),
                "room": lambda x: random.choice(all_rooms),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 25)),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} Created!"))
