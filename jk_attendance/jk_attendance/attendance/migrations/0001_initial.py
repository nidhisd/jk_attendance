# Generated by Django 2.1.5 on 2019-01-25 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_attendance_logged', models.DateTimeField()),
                ('time_of_day', models.CharField(choices=[('AM', 'Morning'), ('PM', 'Evening')], max_length=2)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('dob', models.DateField(null=True)),
                ('barcode', models.IntegerField(default=1234567890, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Participant'),
        ),
    ]
