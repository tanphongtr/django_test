# Generated by Django 3.1.2 on 2020-10-29 10:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('django_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JsonS',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('field1', models.CharField(max_length=255)),
                ('data', models.JSONField()),
            ],
            options={
                'db_table': 'json_s',
            },
        ),
    ]
