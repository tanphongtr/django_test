import uuid
from django.db import models


class JsonS(models.Model):
    class Meta:
        db_table = 'json_s'

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    field1 = models.CharField(max_length=255)
    data = models.JSONField()