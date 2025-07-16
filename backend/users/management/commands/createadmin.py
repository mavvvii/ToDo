import os
import sys

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

UserModel = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if UserModel.objects.using('default').filter(is_superuser = True).count() == 0:
            username: str = os.environ.get('DJANGO_ADMIN_USER', 'admin')
            email: str = os.environ.get('DJANGO_ADMIN_EMAIL', 'admin@example.com')
            password: str = os.environ.get('DJANGO_ADMIN_PASSWORD', 'admin')
            sys.stdout.write(
                f'Creating account for {username} \n'
            )

            admin = UserModel.objects.create_superuser(
                username = username, email = email, password = password 
            )
            admin.save()
        else:
            sys.stdout.write(
                f'There can be only one administrator account! Can not create the other one. \n'
            )
