# Generated by Django 3.1.2 on 2020-10-26 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_timing_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timing',
            name='now',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
    ]
