from django.db import models
from .custom_fields import _models

class DefaultTable(models.Model):
    field4 = _models.DateTimeField()
    class Meta:
        db_table = 'default_tbl'