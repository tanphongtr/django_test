from django.db import models


class UniqueIndex(models.Model):
    sequence = models.CharField(max_length=255)
    stock = models.CharField(max_length=255)

    class Meta:
        unique_together = [
            ("sequence", "stock"),
        ]