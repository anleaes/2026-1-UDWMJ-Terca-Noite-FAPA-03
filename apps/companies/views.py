from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import viewsets
from .serializer import CompanySerializer
from .forms import CompanyForm
from .models import Company


def add_company(request):
    template_name = 'companies/add_company.html'
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('companies:list_companies')
    else:
        form = CompanyForm()
    return render(request, template_name, {'form': form})


def list_companies(request):
    template_name = 'companies/list_companies.html'
    companies = Company.objects.filter()
    context = {'companies': companies}
    return render(request, template_name, context)


def edit_company(request, id_company):
    template_name = 'companies/add_company.html'
    company = get_object_or_404(Company, id=id_company)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('companies:list_companies')
    else:
        form = CompanyForm(instance=company)
    return render(request, template_name, {'form': form})


def delete_company(request, id_company):
    company = get_object_or_404(Company, id=id_company)
    company.delete()
    return redirect('companies:list_companies')


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
