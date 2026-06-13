from rest_framework import serializers
from .models import Inspection


class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = '__all__'


class ClientInspectionSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = ['id', 'visit_date', 'status_found', 'is_compliant', 'score']
