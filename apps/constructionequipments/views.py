from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import viewsets
from constructions.models import Construction
from equipments.models import Equipment
from .forms import ConstructionEquipmentForm
from .models import ConstructionEquipment
from .serializer import ConstructionEquipmentSerializer


def list_constructionequipment(request, construction_id):
    construction = get_object_or_404(Construction, id=construction_id)
    allocations = ConstructionEquipment.objects.filter(construction=construction)
    context = {'construction': construction, 'allocations': allocations}
    return render(request, 'constructionequipments/list_constructionequipment.html', context)


def _available_equipment_queryset(company):
    all_equipment = list(Equipment.objects.filter(company=company))
    available_ids = [e.pk for e in all_equipment if e.is_available]
    return Equipment.objects.filter(pk__in=available_ids)


def add_constructionequipment(request, construction_id):
    construction = get_object_or_404(Construction, id=construction_id)
    template_name = 'constructionequipments/add_constructionequipment.html'
    if request.method == 'POST':
        form = ConstructionEquipmentForm(request.POST)
        form.fields['equipment'].queryset = _available_equipment_queryset(construction.company)
        if form.is_valid():
            allocation = form.save(commit=False)
            allocation.construction = construction
            allocation.return_date = None
            allocation.save()
            allocation.equipment.is_available = False
            allocation.equipment.save()
            messages.success(request, f'Equipamento "{allocation.equipment.name}" alocado com sucesso!')
            return redirect('constructionequipments:list_constructionequipment', construction_id=construction_id)
    else:
        form = ConstructionEquipmentForm()
        form.fields['equipment'].queryset = _available_equipment_queryset(construction.company)
    return render(request, template_name, {'form': form, 'construction': construction})


def edit_constructionequipment(request, construction_id, constructionequipment_id):
    construction = get_object_or_404(Construction, id=construction_id)
    allocation = get_object_or_404(ConstructionEquipment, id=constructionequipment_id, construction=construction)
    template_name = 'constructionequipments/add_constructionequipment.html'
    if request.method == 'POST':
        form = ConstructionEquipmentForm(request.POST, instance=allocation)
        form.fields['equipment'].queryset = Equipment.objects.filter(company=construction.company)
        if form.is_valid():
            updated = form.save(commit=False)
            if updated.return_date:
                days = (updated.return_date - updated.allocation_date).days
                updated.usage_cost = updated.equipment.daily_rate * days
                updated.equipment.is_available = True
                updated.equipment.save()
            updated.save()
            messages.success(request, f'Alocação de "{allocation.equipment.name}" atualizada com sucesso!')
            return redirect('constructionequipments:list_constructionequipment', construction_id=construction_id)
    else:
        form = ConstructionEquipmentForm(instance=allocation)
        form.fields['equipment'].queryset = Equipment.objects.filter(company=construction.company)
    return render(request, template_name, {'form': form, 'construction': construction, 'allocation': allocation})


def delete_constructionequipment(request, construction_id, constructionequipment_id):
    construction = get_object_or_404(Construction, id=construction_id)
    allocation = get_object_or_404(ConstructionEquipment, id=constructionequipment_id, construction=construction)
    allocation.equipment.is_available = True
    allocation.equipment.save()
    allocation.delete()
    messages.success(request, 'Alocação removida e equipamento liberado com sucesso!')
    return redirect('constructionequipments:list_constructionequipment', construction_id=construction_id)


class ConstructionEquipmentViewSet(viewsets.ModelViewSet):
    queryset = ConstructionEquipment.objects.all()
    serializer_class = ConstructionEquipmentSerializer
