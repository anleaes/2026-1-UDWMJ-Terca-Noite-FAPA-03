from .models import AuditReport
from rest_framework import serializers


class AuditReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditReport
        fields = '__all__'
