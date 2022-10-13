from django.urls import path
from velogest.views import velogest_home, sensor_list, SensorView, DeleteSensor, sensor_form, campaign_list, campaign_form, DeleteCampaign, CampaignView

app_name = 'velogest'
urlpatterns = [
    path('', velogest_home, name="home"),
    path('sensor/list', sensor_list, name="list"),
    path('sensor/<int:pk>', SensorView.as_view(), name="sensor_id"),
    path('sensor/<int:pk>/modify', sensor_form, name="modify_sensor"),
    path('sensor/<int:pk>/delete', DeleteSensor.as_view(), name="delete_sensor"),
    path('sensor/add', sensor_form, name="add_sensor"),
    path('campaign/list', campaign_list, name="campaign_list"),
    path('campaign/add', campaign_form, name="add_campaign"),
    path('campaign/<int:pk>', CampaignView.as_view(), name="campaign_id"),
    path('campaign/<int:pk>/modify', campaign_form, name="modify_campaign"),
    path('campaign/<int:pk>/delete',
         DeleteCampaign.as_view(), name="delete_campaign"),
]
