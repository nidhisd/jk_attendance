# Generated by Django 2.1.5 on 2019-01-25 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20190125_1252'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('participant', 'date', 'time_of_day')},
        ),
    ]
