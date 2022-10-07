from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from velogest.models import Sensor
from velogest.forms import SensorForm
from django.shortcuts import resolve_url
from django.views.generic import DeleteView

# Create your views here.


def home(request):
    # return HttpResponse("Home page")
    return HttpResponseRedirect(resolve_url('velogest:list'))


def velogest_home(request):
    return HttpResponse("Velogest home page")


def sensor_list(request):
    sensors = Sensor.objects.all()
    context = {
        "sensors": sensors
    }
    return render(request, 'sensor_list.html', context)


class SensorViewID(View):
    def get(self, request, pk):
        # print(sensor_name)
        sensor = Sensor.objects.get(pk=pk)
        context = {
            "sensor": sensor
        }
        return render(request, 'sensor_detail.html', context)


class SensorView(View):
    def get(self, request, sensor_name):
        # print(sensor_name)
        sensor = Sensor.objects.get(name=sensor_name)
        context = {
            "sensor": sensor
        }
        return render(request, 'sensor_detail.html', context)
        # return HttpResponseRedirect(resolve_url('velogest:sensor', sensor_name))


def sensor(request):
    form = SensorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(resolve_url('velogest:list'))
    return render(request, 'sensor.html', {'form': form})


def modify_sensor(request, pk):
    sensor = Sensor.objects.get(pk=pk)
    form = SensorForm(request.POST or None, instance=sensor)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(resolve_url('velogest:list'))
    return render(request, 'sensor.html', {'form': form})


class DeleteSensor(DeleteView):
    model = Sensor
    template_name = "sensor_deleted.html"
    success_url = "/"
