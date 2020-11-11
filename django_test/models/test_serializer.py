import json
from django.db import models

class TestSerializer(models.Model):

    props1 = models.CharField(max_length=225)

    class Meta:
        db_table = 'test_serializer'

    @property
    def props1_json(self):
        try:
            return json.loads(self.props1.replace("'", "\""))
        except Exception:
            pass
        return