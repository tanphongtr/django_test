from django.db import models
from .parent import Parent

class Child(models.Model):
    class Meta:
        db_table = 'child'

    name = models.CharField(max_length=255)
    parent = models.ForeignKey(Parent, related_name='parent', on_delete=models.CASCADE, null=True, )