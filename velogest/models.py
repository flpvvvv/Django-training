from django.db import models


class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Type1SensorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type='T1')


class Sensor(CommonInfo):
    name = models.CharField(max_length=150)
    # created_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)
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
    owners = models.ManyToManyField(
        'auth.User', related_name='gestion')
    campaign = models.ForeignKey(
        'velogest.Campaign', related_name='campaign', on_delete=models.SET_NULL, null=True, blank=True
    )

    objects = models.Manager()
    type1_sensors = Type1SensorManager()

    def __str__(self):
        return self.name


class Campaign(CommonInfo):
    start_day = models.DateField()
    end_day = models.DateField()


class OrderedByLatitudeType1Sensor(Sensor):
    objects = Sensor.type1_sensors

    class Meta:
        proxy = True
        ordering = ['latitude']
