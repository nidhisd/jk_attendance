# Generated by Django 2.1.5 on 2019-01-25 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date(2019, 1, 25)),
        ),
    ]