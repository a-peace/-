# Generated by Django 3.1.2 on 2020-10-26 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timing',
            name='now',
            field=models.DateField(auto_now=True, verbose_name='Дата создания'),
        ),
    ]