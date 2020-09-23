from django.db import models as md

class Model(md.Model):
    pass

class CharField(md.CharField):
    pass

class DateTimeField(md.Field):
    def db_type(self, connection):
        return 'datetime DEFAULT CURRENT_TIMESTAMP'

    def rel_db_type(self, connection):
        return super().rel_db_type(connection)