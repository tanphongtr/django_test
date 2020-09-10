import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin


class User(models.Model):
    # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

class BaseUser(AbstractBaseUser):
    username = models.CharField(max_length=50)
    class Meta:
        db_table = 'base_users'
    pass