from django.db import models


class File(models.Model):
    class Meta:
        db_table = 'files'

    orginal_name = models.CharField(max_length=255, )
    file_size = models.PositiveIntegerField()
    extensions = models.CharField(max_length=255, )
    file_url = models.FileField(upload_to='files/%Y/%m/%d', )
    created_at = models.DateTimeField(auto_now_add=True, )
    modified_at = models.DateTimeField(auto_now=True, )
