# Generated by Django 3.1.2 on 2020-10-27 01:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20201027_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='now',
            name='now',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 4, 13, 35, 782255)),
        ),
        migrations.AlterField(
            model_name='timing',
            name='penalty',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='Неустойка'),
        ),
    ]
