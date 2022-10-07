
from django import forms

from velogest.models import Sensor
from django.core.exceptions import ValidationError


# class SensorForm(forms.Form):
#     name = forms.CharField(max_length=100, label="Enter the sensor name")
#     latitude = forms.FloatField()
#     longitude = forms.FloatField()
#     type = forms.ChoiceField(
#         choices=[
#             ("T1", "t1"),
#             ("T2", "t2"),
#         ],
#     )

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["name"] = "sensor"

    # def clean(self):
    #     data = super().clean()
    #     if data["latitude"] > 1000:
    #         self.add_error("latitude", ValidationError(
    #             "invalide value", code="invalide"))
