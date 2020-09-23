from django.db import models
# from .parent import Parent

class Child(models.Model):
    class Meta:
        db_table = 'child'

    name = models.CharField(max_length=255)
    # parent = models.ManyToManyField(Parent, related_name='parent')