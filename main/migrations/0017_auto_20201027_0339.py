# Generated by Django 3.1.2 on 2020-10-27 00:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20201027_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='now',
            name='now',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
