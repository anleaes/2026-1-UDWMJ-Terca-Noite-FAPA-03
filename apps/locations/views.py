from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import LocationSerializer
from .forms import LocationForm
from .models import Location


@login_required
def add_location(request):
    template_name = 'locations/add_location.html'
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('locations:list_location')
    else:
        form = LocationForm()
    return render(request, template_name, {'form': form})


@login_required
def list_location(request):
    template_name = 'locations/list_location.html'
    itens = Location.objects.filter()
    context = {'itens': itens}
    return render(request, template_name, context)


@login_required
def edit_location(request, id_location):
    template_name = 'locations/add_location.html'
    location = get_object_or_404(Location, id=id_location)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('locations:list_location')
    else:
        form = LocationForm(instance=location)
    return render(request, template_name, {'form': form})


@login_required
def delete_location(request, id_location):
    location = get_object_or_404(Location, id=id_location)
    location.delete()
    return redirect('locations:list_location')


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
