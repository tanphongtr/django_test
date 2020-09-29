import uuid
from django.db import models
from .user import User

class UserInfo(models.Model):
    # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=16, default='', )
    last_name = models.CharField(max_length=16, default='', )
    
    class Meta:
        db_table = 'user_info'