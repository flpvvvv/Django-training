from django.urls import path
from velogest.views import velogest_home, sensor_list, SensorView

app_name = 'velogest'
urlpatterns = [
    path('', velogest_home, name="home"),
    path('list', sensor_list, name="list"),
    path('sensor/<str:sensor_name>', SensorView.as_view(), name="sensor"),
]
