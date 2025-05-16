from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import os
from django.core.management import call_command
from django.contrib.auth.models import User

class LivestockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'livestock'

    def ready(self):
        pass  # We'll handle superuser creation using a signal

@receiver(post_migrate)
def create_superuser(sender, app_config, **kwargs):
    if app_config.name == 'livestock' and os.environ.get('RENDER') == 'True':
        try:
            if not User.objects.filter(is_superuser=True).exists():
                print("Creating initial superuser...")
                call_command('createsuperuser', '--username=chomba', '--email=chombaerickdickson@gmail.com', '--password=Dickson1')
                print("Superuser created successfully.")
        except (OperationalError, ProgrammingError):
            # Database might not be ready yet during initial setup
            pass