# Generated by Django 5.0.4 on 2024-04-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_order_user_alter_order_vehicle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrating',
            name='rating',
            field=models.IntegerField(choices=[(1, 'Horrible'), (2, 'Bad'), (3, 'Avarage'), (4, 'Good'), (5, 'Excellent')]),
        ),
    ]
