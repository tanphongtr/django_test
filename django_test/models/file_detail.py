from django.db import models
from .file import File

class FileDetail(models.Model):
    class Meta:
        db_table = 'file_details'

    file_name = models.CharField(max_length=255, )
    file = models.OneToOneField(File, on_delete=models.CASCADE, related_name='file', )
    created_at = models.DateTimeField(auto_now_add=True, )
    modified_at = models.DateTimeField(auto_now=True, )
