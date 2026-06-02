from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import viewsets
from .serializer import CitizenSerializer
from .forms import CitizenForm
from .models import Citizen


def add_citizen(request):
    template_name = 'citizens/add_citizen.html'
    if request.method == 'POST':
        form = CitizenForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            messages.success(request, f'Cidadão "{f.first_name} {f.last_name}" adicionado com sucesso!')
            return redirect('citizens:list_citizens')
    else:
        form = CitizenForm()
    return render(request, template_name, {'form': form})


def list_citizens(request):
    template_name = 'citizens/list_citizens.html'
    citizens = Citizen.objects.filter()
    context = {'citizens': citizens}
    return render(request, template_name, context)


def edit_citizen(request, id_citizen):
    template_name = 'citizens/add_citizen.html'
    citizen = get_object_or_404(Citizen, id=id_citizen)
    if request.method == 'POST':
        form = CitizenForm(request.POST, instance=citizen)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cidadão "{citizen.first_name} {citizen.last_name}" atualizado com sucesso!')
            return redirect('citizens:list_citizens')
    else:
        form = CitizenForm(instance=citizen)
    return render(request, template_name, {'form': form, 'citizen': citizen})


def delete_citizen(request, id_citizen):
    citizen = get_object_or_404(Citizen, id=id_citizen)
    citizen_name = f'{citizen.first_name} {citizen.last_name}'
    citizen.delete()
    messages.success(request, f'Cidadão "{citizen_name}" removido com sucesso!')
    return redirect('citizens:list_citizens')


class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
