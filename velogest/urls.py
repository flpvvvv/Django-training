from django.urls import path
from velogest.views import velogest_home, sensor_list, SensorView, SensorViewID, sensor

app_name = 'velogest'
urlpatterns = [
    path('', velogest_home, name="home"),
    path('list', sensor_list, name="list"),
    path('sensor/<str:sensor_name>', SensorView.as_view(), name="sensor"),
    path('sensor_id/<int:pk>', SensorViewID.as_view(), name="sensor_id"),
    path('sensor', sensor, name="sensor_form"),
]
