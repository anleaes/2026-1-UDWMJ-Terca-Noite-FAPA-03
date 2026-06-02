from .models import ConstructionEquipment
from rest_framework import serializers


class ConstructionEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionEquipment
        fields = '__all__'
