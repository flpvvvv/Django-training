from django.db import models

# Create your models here.


class Sensor(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    type = models.CharField(
        max_length=20,
        choices=[
            ("T1", "type 1"),
            ("T2", "type 2"),
            ("T3", "type 3"),
        ],
        default="T2"
    )
    owers = models.ManyToManyField(
        'auth.User', related_name='gestion')
    campaign = models.ForeignKey(
        'velogest.Campaign', related_name='campaign', on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Campaign(models.Model):
    start_day = models.DateField()
    end_day = models.DateField()
