from django.contrib.auth.models import User
from django.db.models import Min, Avg
from rest_framework import serializers
from .models import GPUMetrics, MemoryMetrics, PersonalComputer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']


class ListPersonalComputerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = PersonalComputer
        fields = '__all__'


class PersonalComputerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = PersonalComputer
        fields = ['user']


class GPUMetricSerializer(serializers.ModelSerializer):
    pc = PersonalComputerSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = GPUMetrics
        fields = '__all__'


class MemoryMetricSerializer(serializers.ModelSerializer):
    pc = PersonalComputerSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = MemoryMetrics
        fields = "__all__"


class MinMaxValueGPUSerializer(serializers.ModelSerializer):

    class Meta:
        model = GPUMetrics
        fields = ['gpu_core', 'created_at', 'hour_at']


class MemoryMetricsValuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = MemoryMetrics
        fields = ['used', 'created_at', 'hour_at']