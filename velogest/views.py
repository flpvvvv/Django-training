from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from velogest.models import Sensor
from velogest.forms import SensorForm, FilterForm
from django.shortcuts import resolve_url
from django.views.generic import DeleteView
from django.contrib import messages

# Create your views here.


def home(request):
    # return HttpResponse("Home page")
    return HttpResponseRedirect(resolve_url('velogest:list'))


def velogest_home(request):
    # return HttpResponse("Velogest home page")
    return HttpResponseRedirect(resolve_url('velogest:list'))


def sensor_list(request):
    sensors = Sensor.objects.all()
    form = FilterForm(request.GET or None)
    if form.is_valid():
        # print(form.cleaned_data)
        data = form.cleaned_data
        name = data.get("name")
        campaign = data.get("campaign")
        owners = data.get("owners")
        print(name, campaign, owners)

        if name:
            sensors = sensors.filter(name__icontains=name)
        if campaign:
            sensors = sensors.filter(campaign=campaign)
        if owners:
            sensors = sensors.filter(owners=owners)

    context = {
        "sensors": sensors,
        "form": form,
    }

    return render(request, 'sensor_list.html', context)


class SensorView(View):
    def get(self, request, pk):
        # print(sensor_name)
        sensor = Sensor.objects.get(pk=pk)
        context = {
            "sensor": sensor
        }
        return render(request, 'sensor_detail.html', context)


def sensor_form(request, pk=None):
    if pk:
        sensor = Sensor.objects.get(pk=pk)
    else:
        sensor = None
    form = SensorForm(request.POST or None, instance=sensor)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(resolve_url('velogest:list'))
    return render(request, 'sensor_form.html', {'form': form})


class DeleteSensor(DeleteView):
    model = Sensor
    template_name = "sensor_delete.html"
    # success_url = "/"
    success_url = reverse_lazy('velogest:list')
