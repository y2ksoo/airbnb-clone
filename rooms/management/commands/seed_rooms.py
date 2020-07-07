import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as users_model
from rooms import models as rooms_model


class Command(BaseCommand):

    help = 'This command create facilities"'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many rooms do you want create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        all_users = users_model.User.objects.all()
        room_types = rooms_model.RoomType.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            rooms_model.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(10, 1000),
                "guest": lambda x: random.randint(1, 6),
                "beds": lambda x: random.randint(1, 6),
                "bedrooms": lambda x: random.randint(1, 3),
                "bath": lambda x: random.randint(1, 3),
            },
        )
        created_rooms = seeder.execute()
        created_clean = flatten(list(created_rooms.values()))
        amenities = rooms_model.Amenity.objects.all()
        facilities = rooms_model.Facility.objects.all()
        house_rules = rooms_model.HouseRule.objects.all()

        for pk in created_clean:
            room = rooms_model.Room.objects.get(pk=pk)
            for i in range(3, random.randint(5, 10)):
                rooms_model.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenity.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facility.add(f)
            for r in house_rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.house_rule.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} Rooms Created!"))
