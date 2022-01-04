# Generated by Django 3.2.10 on 2022-01-04 19:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cameras', '0001_initial'),
        ('violations', '0001_initial'),
        ('cars', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fine2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FID', models.IntegerField(unique=True)),
                ('ViolationDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('DriverCarID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
                ('DriverNID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.car_owner')),
            ],
        ),
        migrations.CreateModel(
            name='Fine1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FID', models.IntegerField(unique=True)),
                ('CameraID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cameras.camera')),
                ('ViolationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='violations.violation')),
            ],
            options={
                'unique_together': {('FID', 'CameraID', 'ViolationID')},
            },
        ),
    ]