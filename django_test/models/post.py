import uuid
from django.db import models

class Post(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # author = models.ForeignKey(related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=500)
    # status = models.BooleanField(default=)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    test = models.TextField(max_length=500, null=True, default='ABC')
    test2 = models.TextField(max_length=500, null=False, default='ABC')
    test3 = models.TextField(max_length=500, default='ABC')

    class Meta:
        db_table = 'posts'