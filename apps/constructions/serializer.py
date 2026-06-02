from .models import Construction
from rest_framework import serializers


class ConstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Construction
        fields = '__all__'
