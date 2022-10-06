from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.


class Sensor(models.Model):
    name = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    type = models.CharField(
        max_length=20,
        choices=[
            ("T1", "t1"),
            ("T2", "t2"),
        ],
        default="T1"
    )

    def __str__(self):
        return self.name
