from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.


class Sensor(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
