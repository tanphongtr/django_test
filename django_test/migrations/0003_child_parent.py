# Generated by Django 3.1.1 on 2020-09-16 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_test', '0002_auto_20200914_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'parent',
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ManyToManyField(related_name='parent', to='django_test.Parent')),
            ],
            options={
                'db_table': 'child',
            },
        ),
    ]
