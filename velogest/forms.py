
from django import forms

from velogest.models import Sensor


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
