from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from constructions.models import Construction
from .forms import InspectionForm
from .models import Inspection
from .serializer import InspectionSerializer


def list_inspection(request, construction_id):
    construction = get_object_or_404(Construction, id=construction_id)
    inspections = Inspection.objects.filter(construction=construction)
    context = {'construction': construction, 'inspections': inspections}
    return render(request, 'inspections/list_inspection.html', context)


def add_inspection(request, construction_id):
    construction = get_object_or_404(Construction, id=construction_id)
    template_name = 'inspections/add_inspection.html'
    if request.method == 'POST':
        form = InspectionForm(request.POST)
        form.fields['employee'].queryset = construction.company.employee_set.all()
        if form.is_valid():
            inspection = form.save(commit=False)
            inspection.construction = construction
            inspection.save()
            return redirect('inspections:list_inspection', construction_id=construction_id)
    else:
        form = InspectionForm()
        form.fields['employee'].queryset = construction.company.employee_set.all()
    return render(request, template_name, {'form': form, 'construction': construction})


def edit_inspection(request, construction_id, id_inspection):
    construction = get_object_or_404(Construction, id=construction_id)
    inspection = get_object_or_404(Inspection, id=id_inspection, construction=construction)
    template_name = 'inspections/add_inspection.html'
    if request.method == 'POST':
        form = InspectionForm(request.POST, instance=inspection)
        form.fields['employee'].queryset = construction.company.employee_set.all()
        if form.is_valid():
            form.save()
            return redirect('inspections:list_inspection', construction_id=construction_id)
    else:
        form = InspectionForm(instance=inspection)
        form.fields['employee'].queryset = construction.company.employee_set.all()
    return render(request, template_name, {'form': form, 'construction': construction, 'inspection': inspection})


def delete_inspection(request, construction_id, id_inspection):
    construction = get_object_or_404(Construction, id=construction_id)
    inspection = get_object_or_404(Inspection, id=id_inspection, construction=construction)
    inspection.delete()
    return redirect('inspections:list_inspection', construction_id=construction_id)


class InspectionViewSet(viewsets.ModelViewSet):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer
