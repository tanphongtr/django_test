import uuid
from ..models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(Use,)
    full_name = models.CharField(max_length=32)

    class Meta:
        db_table = 'profiles'