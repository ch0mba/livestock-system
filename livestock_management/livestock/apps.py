from django.apps import AppConfig

from django.db.utils import OperationalError, ProgrammingError

from django.contrib.auth.models import User
 
class LivestockConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'

    name = 'livestock'
 
    