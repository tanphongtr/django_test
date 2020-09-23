from django.db import models

class DateTimeField(models.DateTimeField):

    def db_type(self, connection):
        return 'datetime DEFAULT CURRENT_TIMESTAMP'

    def rel_db_type(self, connection):
        return super().rel_db_type(connection)