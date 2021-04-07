from rest_framework import serializers
from .models import GPUMetrics
from pc.models import PersonalComputer


class PersonalComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalComputer
        exclude = ['updated_at', 'created_at']


class GPUMetricSerializer(serializers.ModelSerializer):
    # pc = PersonalComputerSerializer()
    # Ou Read only field
    # gpu = serializers.ReadOnlyField(source='pc.gpu')
    pc = PersonalComputerSerializer(read_only=True)
    class Meta:
        model = GPUMetrics
        #exclude = ['pc']
        fields = ['gpu_core', 'gpu_memory', 'gpu_vrm_core', 'gpu_hot_spot', 'pc']

