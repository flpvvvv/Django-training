# Generated by Django 4.1.2 on 2022-10-06 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velogest', '0002_alter_sensor_created_at_alter_sensor_modified_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='type',
            field=models.CharField(choices=[('T1', 't1'), ('T2', 't2')], default='T1', max_length=20),
        ),
    ]