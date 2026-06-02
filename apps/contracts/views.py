from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import viewsets
from .forms import ContractForm
from .models import Contract
from .serializer import ContractSerializer
from constructions.models import Construction


def list_contracts(request, construction_id):
    construction = get_object_or_404(Construction, id=construction_id)
    contracts = Contract.objects.filter(construction=construction)
    context = {
        'construction': construction,
        'contracts': contracts
    }
    return render(request, 'contracts/list_contracts.html', context)


def add_contract(request, construction_id):
    construction = get_object_or_404(Construction, id=construction_id)
    template_name = 'contracts/add_contract.html'

    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.construction = construction
            contract.save()
            messages.success(request, f'Contrato "{contract.number}" adicionado com sucesso!')
            return redirect('contracts:list_contracts', construction_id=construction_id)
    else:
        form = ContractForm()

    context = {'form': form, 'construction': construction}
    return render(request, template_name, context)


def edit_contract(request, construction_id, id_contract):
    construction = get_object_or_404(Construction, id=construction_id)
    contract = get_object_or_404(Contract, id=id_contract, construction=construction)
    template_name = 'contracts/add_contract.html'

    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            form.save()
            messages.success(request, f'Contrato "{contract.number}" atualizado com sucesso!')
            return redirect('contracts:list_contracts', construction_id=construction_id)
    else:
        form = ContractForm(instance=contract)

    context = {'form': form, 'construction': construction, 'contract': contract}
    return render(request, template_name, context)


def delete_contract(request, construction_id, id_contract):
    construction = get_object_or_404(Construction, id=construction_id)
    contract = get_object_or_404(Contract, id=id_contract, construction=construction)
    contract.delete()
    messages.success(request, f'Contrato "{contract.number}" removido com sucesso!')
    return redirect('contracts:list_contracts', construction_id=construction_id)


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
