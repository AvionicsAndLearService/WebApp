# Generated by Django 3.0.7 on 2021-05-27 02:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basedatos', '0010_auto_20210526_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ot',
            name='cliente',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ot',
            name='hangar',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ot',
            name='matricula',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ot',
            name='modelo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ot',
            name='observacion',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='ot',
            name='orden_ALS',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ot',
            name='serie',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ot',
            name='tecnicos',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
