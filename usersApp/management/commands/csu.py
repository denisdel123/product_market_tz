import os

from django.core.management import BaseCommand
from usersApp.models import User
from dotenv import load_dotenv
load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            first_name='Admin',
            email='admin@mail.ru',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        user.set_password(os.environ.get('PASS_SUPERUSER'))
        user.save()
