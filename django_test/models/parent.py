from django.db import models
from .child import Child

class Parent(models.Model):
    class Meta:
        db_table = 'parent'
    
    name = models.CharField(max_length=255)
    child = models.ManyToManyField(Child, related_name='child', )