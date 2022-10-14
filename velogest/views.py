from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from velogest.models import Sensor, Campaign
from velogest.forms import SensorForm, FilterForm, CampaignForm
from django.shortcuts import resolve_url
from django.views.generic import DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin


def home(request):
    # return HttpResponse("Home page")
    return HttpResponseRedirect(resolve_url('velogest:list'))


def velogest_home(request):
    # return HttpResponse("Velogest home page")
    return HttpResponseRedirect(resolve_url('velogest:list'))


@login_required
def sensor_list(request):
    sensors = Sensor.objects.all()
    form = FilterForm(request.GET or None)
    if form.is_valid():
        data = form.cleaned_data
        name = data.get("name")
        campaign = data.get("campaign")
        owners = data.get("owners")

        if name:
            sensors = sensors.filter(name__icontains=name)
        if campaign:
            sensors = sensors.filter(campaign=campaign)
        if owners:
            sensors = sensors.filter(owners=owners)

        if data.get('created_at_after'):
            sensors = sensors.filter(
                created_at__date__gte=data.get('created_at_after'))
        if data.get('created_at_before'):
            sensors = sensors.filter(
                created_at__date__lte=data.get('created_at_before'))

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
        if pk:
            messages.success(request, "Sensor modified successfully")
        else:
            messages.success(request, "Sensor added successfully")
        return HttpResponseRedirect(resolve_url('velogest:list'))
    return render(request, 'sensor_form.html', {'form': form})


class DeleteSensor(SuccessMessageMixin, DeleteView):
    model = Sensor
    template_name = "sensor_delete.html"
    # success_url = "/"
    success_url = reverse_lazy('velogest:list')
    success_message = "Sensor is successfully deleted."


@permission_required('velogest.add_campaign', raise_exception=True)
def campaign_form(request, pk=None):
    if pk and not request.user.has_perm('velogest.change_campaign'):
        raise PermissionDenied("Permission Denied")

    if pk:
        campaign = Campaign.objects.get(pk=pk)
    else:
        campaign = None
    form = CampaignForm(request.POST or None, instance=campaign)

    if form.is_valid():
        form.save()
        if pk:
            messages.success(request, "Campaign modified successfully")
        else:
            messages.success(request, "Campaign added successfully")
        return HttpResponseRedirect(resolve_url('velogest:campaign_list'))
    return render(request, 'campaign_form.html', {'form': form})


def campaign_list(request):
    campaigns = Campaign.objects.all()

    context = {
        "campaigns": campaigns,
    }

    return render(request, 'campaign_list.html', context)


class CampaignView(View):
    def get(self, request, pk):
        # print(sensor_name)
        campaign = Campaign.objects.get(pk=pk)
        context = {
            "campaign": campaign
        }
        return render(request, 'campaign_detail.html', context)


class DeleteCampaign(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Campaign
    template_name = "campaign_delete.html"
    # success_url = "/"
    success_url = reverse_lazy('velogest:campaign_list')
    success_message = "Campaign is successfully deleted."
    permission_required = 'velogest.delete_campaign'
