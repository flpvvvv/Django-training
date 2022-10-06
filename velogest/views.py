from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from velogest.models import Sensor

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
