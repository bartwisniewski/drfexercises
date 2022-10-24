from django.views.generic import ListView
from .models import Valve, Pump


class ValvesListView(ListView):
    model = Valve
    context_object_name = 'valves'
    template_name = 'processautomation/valves.html'


class PumpsListView(ListView):
    model = Pump
    context_object_name = 'pumps'
    template_name = 'processautomation/pumps.html'
