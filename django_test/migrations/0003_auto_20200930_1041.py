# Generated by Django 3.1.1 on 2020-09-30 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_test', '0002_auto_20200930_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniqueindex',
            name='sequence',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='uniqueindex',
            name='stock',
            field=models.CharField(max_length=255),
        ),
    ]
