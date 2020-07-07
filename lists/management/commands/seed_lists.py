import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists.models import List
from users import models as users_model
from rooms import models as rooms_model

NAME = "lists"


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
            List, number, {"user": lambda x: random.choice(all_users),},
        )

        created = seeder.execute()
        cleaned = flatten(list(created.values()))

        for pk in cleaned:
            list_model = List.objects.get(pk=pk)
            to_add = all_rooms[random.randint(0, 3) : random.randint(4, 10)]
            list_model.rooms.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} Created!"))
