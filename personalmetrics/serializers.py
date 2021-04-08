from rest_framework import serializers
from .models import GPUMetrics, MemoryMetrics, PersonalComputer


class GPUMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPUMetrics
        exclude = ['pc']


class MemoryMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryMetrics
        exclude = ['pc']


class PersonalComputerSerializer(serializers.ModelSerializer):
    gpu_temps = GPUMetricSerializer(read_only=True, many=True)
    memory_temps = MemoryMetricSerializer(read_only=True, many=True)
    class Meta:
        model = PersonalComputer
        fields = '__all__'
