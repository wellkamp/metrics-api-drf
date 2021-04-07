from rest_framework import serializers
from metrics.models import GPUMetrics
from .models import PersonalComputer


class GPUMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPUMetrics
        exclude = ['pc']


class PersonalComputerSerializer(serializers.ModelSerializer):
    gpu_temps = GPUMetricSerializer(read_only=True, many=True)
    class Meta:
        model = PersonalComputer
        fields = '__all__'
