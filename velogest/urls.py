from django.urls import path
from velogest.views import velogest_home, sensor_list, SensorView, DeleteSensor, sensor_form

app_name = 'velogest'
urlpatterns = [
    path('', velogest_home, name="home"),
    path('list', sensor_list, name="list"),
    path('sensor/<int:pk>', SensorView.as_view(), name="sensor_id"),
    path('sensor/<int:pk>/modify', sensor_form, name="modify_sensor"),
    path('sensor/<int:pk>/delete', DeleteSensor.as_view(), name="delete_sensor"),
    path('sensor/add', sensor_form, name="add_sensor"),
]
