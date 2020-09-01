import uuid
from .album import Album
from django.db import models

class Track(models.Model):
    album = models.OneToOneField(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']
        db_table = 'tracks'

    def __str__(self):
        return '%d: %s' % (self.order, self.title)