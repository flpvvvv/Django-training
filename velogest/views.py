from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from velogest.models import Sensor
from django.shortcuts import resolve_url

# Create your views here.


def home(request):
    return HttpResponse("Home page")


def velogest_home(request):
    return HttpResponse("Velogest home page")


def sensor_list(request):
    sensors = Sensor.objects.all()
    context = {
        "sensors": sensors
    }
    return render(request, 'sensor_list.html', context)


class SensorView(View):
    def get(self, request, sensor_name):
        # print(sensor_name)
        sensor = Sensor.objects.get(name=sensor_name)
        context = {
            "sensor_name": sensor.name,
            "sensor_type": sensor.type,
            "latitude": sensor.latitude,
            "longitude": sensor.longitude,
        }
        return render(request, 'sensor_detail.html', context)
        # return HttpResponseRedirect(resolve_url('velogest:sensor', sensor_name))
