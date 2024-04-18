# Generated by Django 5.0.4 on 2024-04-18 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='currency',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.RESTRICT, to='accounts.currency'),
            preserve_default=False,
        ),
    ]