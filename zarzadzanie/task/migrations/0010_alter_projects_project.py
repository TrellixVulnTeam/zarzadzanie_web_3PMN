# Generated by Django 3.2.9 on 2021-12-14 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_auto_20211130_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
