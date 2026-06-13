from rest_framework import serializers
from .models import Construction


class ConstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Construction
        fields = '__all__'


class ClientConstructionSerializer(serializers.ModelSerializer):
    location_city         = serializers.CharField(source='location.city', read_only=True)
    location_name         = serializers.CharField(source='location.name', read_only=True)
    location_neighborhood = serializers.CharField(source='location.neighborhood', read_only=True)

    class Meta:
        model = Construction
        fields = [
            'id', 'title', 'type', 'status',
            'start_date', 'expected_end_date', 'is_completed',
            'photo',
            'location_city', 'location_name', 'location_neighborhood',
        ]


class ClientConstructionDetailSerializer(ClientConstructionSerializer):
    inspections = serializers.SerializerMethodField()

    def get_inspections(self, obj):
        from inspections.models import Inspection
        from inspections.serializer import ClientInspectionSummarySerializer
        qs = Inspection.objects.filter(construction=obj).order_by('-visit_date')
        return ClientInspectionSummarySerializer(qs, many=True).data

    class Meta(ClientConstructionSerializer.Meta):
        fields = ClientConstructionSerializer.Meta.fields + ['inspections']
