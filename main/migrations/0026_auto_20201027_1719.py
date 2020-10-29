# Generated by Django 3.1.2 on 2020-10-27 14:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20201027_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='now',
            name='now',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 19, 12, 471966)),
        ),
        migrations.AlterField(
            model_name='timing',
            name='days',
            field=models.IntegerField(default=0, verbose_name='Дни разницы'),
        ),
        migrations.AlterField(
            model_name='timing',
            name='delivered',
            field=models.IntegerField(default=0, verbose_name='Доставлено'),
        ),
    ]