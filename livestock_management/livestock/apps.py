from django.apps import AppConfig

from django.db.utils import OperationalError, ProgrammingError

from django.contrib.auth.models import User
 
class LivestockConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'

    name = 'livestock'
 
    def ready(self):

        import os

        if os.environ.get('RENDER') == 'True':  # Check if running on Render

            from django.core.management import call_command

            try:

                if not User.objects.filter(is_superuser=True).exists():

                    print("Creating initial superuser...")

                    call_command('createsuperuser', '--username=chomba', '--email=chombaerickdickson@gmail.com', '--password=Dickson1')

                    print("Superuser created successfully.")

            except (OperationalError, ProgrammingError):

                # Database might not be ready yet during initial setup

                pass
 