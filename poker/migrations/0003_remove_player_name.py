# Generated by Django 2.0.6 on 2018-11-16 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0002_auto_20181116_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='name',
        ),
    ]