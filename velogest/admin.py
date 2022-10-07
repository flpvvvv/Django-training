from django.contrib import admin
from velogest.models import Sensor, Compaign

# Register your models here.


class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'created_at', 'modified_at']
    readonly_fields = ['created_at', 'modified_at']
    list_filter = ['type']


class CompaignAdmin(admin.ModelAdmin):
    list_display = ['start_day', 'end_day']


admin.site.register(Sensor, SensorAdmin)
admin.site.register(Compaign, CompaignAdmin)
