
from django import forms

from velogest.models import Sensor, Campaign
from django.contrib.auth.models import User
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


class FilterForm(forms.Form):
    name = forms.CharField(label="Search by sensor name", required=False)
    campaign = forms.ModelChoiceField(Campaign.objects.all(), required=False)
    owners = forms.ModelChoiceField(User.objects.all(), required=False)
    created_at_after = forms.DateField(required=False)
    created_at_before = forms.DateField(required=False)
