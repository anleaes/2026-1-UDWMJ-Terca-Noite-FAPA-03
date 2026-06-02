from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import viewsets
from .serializer import EquipmentSerializer
from companies.models import Company
from .models import Equipment
from .forms import EquipmentForm


def list_equipments(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    equipments = Equipment.objects.filter(company=company)
    context = {
        'company': company,
        'equipments': equipments
    }
    return render(request, 'equipments/list_equipments.html', context)


def add_equipment(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    template_name = 'equipments/add_equipment.html'

    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.company = company
            equipment.save()
            messages.success(request, f'Equipamento "{equipment.name}" adicionado com sucesso!')
            return redirect('equipments:list_equipments', company_id=company_id)
    else:
        form = EquipmentForm()

    context = {'form': form, 'company': company}
    return render(request, template_name, context)


def edit_equipment(request, company_id, equipment_id):
    company = get_object_or_404(Company, id=company_id)
    equipment = get_object_or_404(Equipment, id=equipment_id, company=company)
    template_name = 'equipments/add_equipment.html'

    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            messages.success(request, f'Equipamento "{equipment.name}" atualizado com sucesso!')
            return redirect('equipments:list_equipments', company_id=company_id)
    else:
        form = EquipmentForm(instance=equipment)

    context = {'form': form, 'company': company, 'equipment': equipment}
    return render(request, template_name, context)


def delete_equipment(request, company_id, equipment_id):
    company = get_object_or_404(Company, id=company_id)
    equipment = get_object_or_404(Equipment, id=equipment_id, company=company)
    equipment.delete()
    messages.success(request, f'Equipamento "{equipment.name}" removido com sucesso!')
    return redirect('equipments:list_equipments', company_id=company_id)


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
