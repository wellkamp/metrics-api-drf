from rest_framework import serializers
from .models import GPUMetrics, MemoryMetrics, PersonalComputer


class ListPersonalComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalComputer
        fields = '__all__'


class GPUMetricSerializer(serializers.ModelSerializer):
    pc = ListPersonalComputerSerializer(read_only=True)
    class Meta:
        model = GPUMetrics
        fields = "__all__"


class MemoryMetricSerializer(serializers.ModelSerializer):
    pc = ListPersonalComputerSerializer(read_only=True)
    class Meta:
        model = MemoryMetrics
        fields = "__all__"


class PersonalComputerSerializer(serializers.ModelSerializer):
    gpu_temps = GPUMetricSerializer(read_only=True, many=True)
    memory_temps = MemoryMetricSerializer(read_only=True, many=True)
    class Meta:
        model = PersonalComputer
        fields = '__all__'
