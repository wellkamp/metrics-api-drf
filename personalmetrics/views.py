from rest_framework import viewsets, generics
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import PersonalComputer, GPUMetrics
from .serializers import PersonalComputerSerializer, GPUMetricSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class PCViewSet(viewsets.ModelViewSet):
    queryset = PersonalComputer.objects.all()
    serializer_class = PersonalComputerSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class GPUMetricViewSet(ReadOnlyModelViewSet):
    serializer_class = PersonalComputerSerializer
    queryset = GPUMetrics.objects.all()
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
