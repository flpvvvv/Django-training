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
        self.fields['campaign'].queryset = Campaign.current_campaign_manager

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


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = '__all__'

    def clean(self):
        data = super().clean()
        if data["start_day"] > data["end_day"]:
            self.add_error("end_day", ValidationError(
                "End day should be later than start day !", code="invalid"))
