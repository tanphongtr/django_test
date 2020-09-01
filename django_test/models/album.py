import uuid
from django.db import models

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'albums'