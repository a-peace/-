# Generated by Django 3.1.2 on 2020-10-27 00:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20201027_0318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='now',
            name='now_time',
        ),
        migrations.AddField(
            model_name='now',
            name='now',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 3, 20, 8, 585600)),
        ),
    ]
