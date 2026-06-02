from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .forms import IncidentForm
from .models import Incident
from .serializer import IncidentSerializer


def add_incident(request):
    template_name = 'incidents/add_incident.html'
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('incidents:list_incidents')
    else:
        form = IncidentForm()
    return render(request, template_name, {'form': form})


def list_incidents(request):
    template_name = 'incidents/list_incidents.html'
    incidents = Incident.objects.filter()
    context = {'incidents': incidents}
    return render(request, template_name, context)


def edit_incident(request, id_incident):
    template_name = 'incidents/add_incident.html'
    incident = get_object_or_404(Incident, id=id_incident)
    if request.method == 'POST':
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            form.save()
            return redirect('incidents:list_incidents')
    else:
        form = IncidentForm(instance=incident)
    return render(request, template_name, {'form': form})


def delete_incident(request, id_incident):
    incident = get_object_or_404(Incident, id=id_incident)
    incident.delete()
    return redirect('incidents:list_incidents')


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
