from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ConstructionSerializer, ClientConstructionSerializer, ClientConstructionDetailSerializer
from .forms import ConstructionForm
from .models import Construction


@login_required
def add_construction(request):
    template_name = 'constructions/add_construction.html'
    if request.method == 'POST':
        form = ConstructionForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('constructions:list_constructions')
    else:
        form = ConstructionForm()
    return render(request, template_name, {'form': form})


@login_required
def list_constructions(request):
    template_name = 'constructions/list_constructions.html'
    constructions = Construction.objects.filter()
    context = {'constructions': constructions}
    return render(request, template_name, context)


@login_required
def edit_construction(request, id_construction):
    template_name = 'constructions/add_construction.html'
    construction = get_object_or_404(Construction, id=id_construction)
    if request.method == 'POST':
        form = ConstructionForm(request.POST, request.FILES, instance=construction)
        if form.is_valid():
            form.save()
            return redirect('constructions:list_constructions')
    else:
        form = ConstructionForm(instance=construction)
    return render(request, template_name, {'form': form})


@login_required
def delete_construction(request, id_construction):
    construction = get_object_or_404(Construction, id=id_construction)
    construction.delete()
    return redirect('constructions:list_constructions')


class ConstructionViewSet(viewsets.ModelViewSet):
    queryset = Construction.objects.all()
    serializer_class = ConstructionSerializer


@api_view(['GET'])
def client_construction_list(request):
    qs = Construction.objects.select_related('location').all()
    data = ClientConstructionSerializer(qs, many=True, context={'request': request}).data
    return Response(data)


@api_view(['GET'])
def client_construction_detail(request, pk):
    obj = get_object_or_404(Construction.objects.select_related('location'), pk=pk)
    data = ClientConstructionDetailSerializer(obj, context={'request': request}).data
    return Response(data)
