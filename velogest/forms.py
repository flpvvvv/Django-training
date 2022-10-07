
from django import forms

from velogest.models import Sensor
from django.core.exceptions import ValidationError

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].initial = "sensor"

    # Valide input
    def clean(self):
        data = super().clean()
        if data["latitude"] > 1000:
            self.add_error("latitude", ValidationError(
                "Invalid value", code="invalid"))
        if data["longitude"] > 1000:
            self.add_error("longitude", ValidationError(
                "Invalid value", code="invalid"))