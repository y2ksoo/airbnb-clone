import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews.models import Review
from users import models as users_model
from rooms import models as rooms_model


class Command(BaseCommand):

    help = 'This command create reviews"'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many reviews do you want create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        all_users = users_model.User.objects.all()
        all_rooms = rooms_model.Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            Review,
            number,
            {
                "accuracy": lambda x: random.randint(0, 6),
                "communication": lambda x: random.randint(0, 6),
                "cleanliness": lambda x: random.randint(0, 6),
                "location": lambda x: random.randint(0, 6),
                "check_in": lambda x: random.randint(0, 6),
                "value": lambda x: random.randint(0, 6),
                "user": lambda x: random.choice(all_users),
                "room": lambda x: random.choice(all_rooms),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} Reviews Created!"))
