# Generated by Django 5.0.4 on 2024-04-15 20:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('vehicles', '0003_alter_vehicle_location_alter_vehicle_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle'),
        ),
        migrations.AlterField(
            model_name='userrating',
            name='reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userrating',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vehiclereview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vehiclereview',
            name='vehicle',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle'),
        ),
    ]
