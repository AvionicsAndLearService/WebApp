# Generated by Django 3.0.7 on 2021-05-27 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basedatos', '0007_auto_20210526_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ot',
            name='hangar',
        ),
        migrations.RemoveField(
            model_name='ot',
            name='observaciones',
        ),
        migrations.RemoveField(
            model_name='ot',
            name='orden',
        ),
    ]