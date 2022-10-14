from django.contrib import admin
from velogest.models import Sensor, Campaign, Observation

# Register your models here.


class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'created_at', 'modified_at']
    readonly_fields = ['created_at', 'modified_at']
    list_filter = ['type']


class CampaignAdmin(admin.ModelAdmin):
    list_display = ['start_day', 'end_day']

class ObservationAdmin(admin.ModelAdmin):
    list_display = ['sensor', 'record_time', 'record_number']


admin.site.register(Sensor, SensorAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Observation, ObservationAdmin)
