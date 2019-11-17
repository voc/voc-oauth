from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='username of the new user')
        parser.add_argument('email', type=str, help='eamil address')
        parser.add_argument('-f', '--firstname', type=str, default='', help='Fist Name')
        parser.add_argument('-n', '--lastname', type=str, default='', help='Last Name')
        parser.add_argument('-a', '--admin', action='store_true', default=False, help='Create an admin account')
        parser.add_argument('-s', '--staff', action='store_true', default=False, help='Create an staff account (access to /admin)')
        parser.add_argument('-d', '--disabled', action='store_true', default=False, help='Create an disabled account')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        admin = kwargs['admin']
        email = kwargs['email']
        firstname = kwargs['firstname']
        lastname = kwargs['lastname']
        staff = kwargs['staff']
        disabled = kwargs['disabled']

        password = None


        if admin:
            User.objects.create_superuser(username=username, email=email, password=password, first_name=firstname, last_name=lastname, is_staff=staff, is_active=not disabled)
        else:
            User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname, is_staff=staff, is_active=not disabled)
