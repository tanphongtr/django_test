import uuid
from .album import Album
from django.db import models

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.SET_NULL, null=True)
    order = models.PositiveIntegerField()
    test = models.PositiveBigIntegerField()
    title = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()

    class Meta:
        # unique_together = ['album', 'order']
        ordering = ['order']
        db_table = 'tracks'

    def __str__(self):
        return '%d: %s' % (self.order, self.title)