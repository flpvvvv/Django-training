# Generated by Django 4.1.2 on 2022-10-07 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velogest', '0003_sensor_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
