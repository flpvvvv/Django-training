from django.contrib import admin
from velogest.models import Sensor

# Register your models here.


class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'created_at', 'modified_at']
    readonly_fields = ['created_at', 'modified_at']
    list_filter = ['type']


admin.site.register(Sensor, SensorAdmin)
