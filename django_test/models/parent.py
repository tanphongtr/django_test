from django.db import models

class Parent(models.Model):
    class Meta:
        db_table = 'parent'
    
    name = models.CharField(max_length=255)