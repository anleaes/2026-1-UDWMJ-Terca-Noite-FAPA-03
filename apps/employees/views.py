from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import viewsets
from .serializer import EmployeeSerializer
from .forms import EmployeeForm
from .models import Employee
from companies.models import Company


def list_employees(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    employees = Employee.objects.filter(company=company)
    context = {'company': company, 'employees': employees}
    return render(request, 'employees/list_employees.html', context)


def add_employee(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    template_name = 'employees/add_employee.html'
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.company = company
            employee.save()
            form.save_m2m()
            messages.success(request, f'Funcionário "{employee.first_name} {employee.last_name}" adicionado com sucesso!')
            return redirect('employees:list_employees', company_id=company_id)
    else:
        form = EmployeeForm()
    return render(request, template_name, {'form': form, 'company': company})


def edit_employee(request, company_id, employee_id):
    company = get_object_or_404(Company, id=company_id)
    employee = get_object_or_404(Employee, id=employee_id, company=company)
    template_name = 'employees/add_employee.html'
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, f'Funcionário "{employee.first_name} {employee.last_name}" atualizado com sucesso!')
            return redirect('employees:list_employees', company_id=company_id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, template_name, {'form': form, 'company': company, 'employee': employee})


def delete_employee(request, company_id, employee_id):
    company = get_object_or_404(Company, id=company_id)
    employee = get_object_or_404(Employee, id=employee_id, company=company)
    employee.delete()
    messages.success(request, f'Funcionário "{employee.first_name} {employee.last_name}" removido com sucesso!')
    return redirect('employees:list_employees', company_id=company_id)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
