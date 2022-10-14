from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from velogest.models import Observation, Sensor, Campaign
from velogest.forms import SensorForm, FilterForm, CampaignForm
from django.shortcuts import resolve_url
from django.views.generic import DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
import json


def home(request):
    # return HttpResponse("Home page")
    return HttpResponseRedirect(resolve_url('velogest:dashboard'))


def velogest_home(request):
    # return HttpResponse("Velogest home page")
    return HttpResponseRedirect(resolve_url('velogest:dashboard'))


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
        # user_li = sensor.owners.all().values_list('username', flat=True)
        # if str(request.user) not in user_li:
        if not request.user.is_superuser and request.user not in sensor.owners.all():
            raise PermissionDenied("Permission Denied")
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


class DeleteSensor(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Sensor
    template_name = "sensor_delete.html"
    # success_url = "/"
    success_url = reverse_lazy('velogest:list')
    success_message = "Sensor is successfully deleted."

    def test_func(self):
        return self.request.user.is_superuser or self.request.user in self.get_object().owners.all()


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


def dashboard(request):
    sensors = Sensor.objects.all()

    context = {
        "sensors": sensors,
    }

    return render(request, 'dashboard.html', context)


def observations_ajax(request):
    sensor_id = request.GET.get("sensor_id")
    if not sensor_id:
        return HttpResponse(status=400)
    observations = Observation.objects.filter(
        sensor_id=sensor_id).order_by('record_time').values_list('record_time', 'record_number')
    values = {
        'dates': [obs[0] for obs in observations],
        'comptes': [obs[1] for obs in observations],
    }
    return JsonResponse(values)
