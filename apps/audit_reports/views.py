from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from constructions.models import Construction
from inspections.models import Inspection
from .forms import AuditReportForm
from .models import AuditReport
from .serializer import AuditReportSerializer


def add_audit_report(request, construction_id, inspection_id):
    construction = get_object_or_404(Construction, id=construction_id)
    inspection = get_object_or_404(Inspection, id=inspection_id, construction=construction)
    if hasattr(inspection, 'auditreport'):
        return redirect('audit_reports:edit_audit_report', construction_id=construction_id, inspection_id=inspection_id)
    template_name = 'audit_reports/add_audit_report.html'
    if request.method == 'POST':
        form = AuditReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.inspection = inspection
            report.save()
            return redirect('inspections:list_inspection', construction_id=construction_id)
    else:
        form = AuditReportForm()
    return render(request, template_name, {'form': form, 'construction': construction, 'inspection': inspection})


def edit_audit_report(request, construction_id, inspection_id):
    construction = get_object_or_404(Construction, id=construction_id)
    inspection = get_object_or_404(Inspection, id=inspection_id, construction=construction)
    audit_report = get_object_or_404(AuditReport, inspection=inspection)
    template_name = 'audit_reports/add_audit_report.html'
    if request.method == 'POST':
        form = AuditReportForm(request.POST, instance=audit_report)
        if form.is_valid():
            form.save()
            return redirect('inspections:list_inspection', construction_id=construction_id)
    else:
        form = AuditReportForm(instance=audit_report)
    return render(request, template_name, {'form': form, 'construction': construction, 'inspection': inspection, 'audit_report': audit_report})


def delete_audit_report(request, construction_id, inspection_id):
    construction = get_object_or_404(Construction, id=construction_id)
    inspection = get_object_or_404(Inspection, id=inspection_id, construction=construction)
    audit_report = get_object_or_404(AuditReport, inspection=inspection)
    audit_report.delete()
    return redirect('inspections:list_inspection', construction_id=construction_id)


class AuditReportViewSet(viewsets.ModelViewSet):
    queryset = AuditReport.objects.all()
    serializer_class = AuditReportSerializer
