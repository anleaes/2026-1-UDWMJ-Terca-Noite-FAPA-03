from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'audit_reports'

router = routers.SimpleRouter()
router.register('', views.AuditReportViewSet, basename='audit_reports')

urlpatterns = [
    path('<int:construction_id>/<int:inspection_id>/add/', views.add_audit_report, name='add_audit_report'),
    path('<int:construction_id>/<int:inspection_id>/edit/', views.edit_audit_report, name='edit_audit_report'),
    path('<int:construction_id>/<int:inspection_id>/delete/', views.delete_audit_report, name='delete_audit_report'),
    path('', include(router.urls)),
]
