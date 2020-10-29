# Generated by Django 3.1.2 on 2020-10-27 01:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20201027_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='timing',
            name='days',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Дни разницы'),
        ),
        migrations.AlterField(
            model_name='now',
            name='now',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 4, 56, 57, 236887)),
        ),
    ]