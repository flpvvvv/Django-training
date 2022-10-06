from django.urls import path
from velogest.views import velogest_home, sensor_list

app_name = 'velogest'
urlpatterns = [
    path('', velogest_home, name="home" ),
    path('list', sensor_list, name='list'),
]