# Generated by Django 4.1.2 on 2022-10-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velogest', '0005_alter_sensor_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
            ],
        ),
    ]
