from rest_framework import serializers
from .models import GPUMetrics


class GPUMetricSerializer(serializers.ModelSerializer):
    # gpu_name = serializers.ReadOnlyField(source='gpu_name.gpu_name')
    class Meta:
        model = GPUMetrics
        exclude = ['updated_at']
