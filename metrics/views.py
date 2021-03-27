from rest_framework import viewsets, generics
from .models import GPUMetrics
from .serializer import GPUMetricSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class GPUMetricsList(generics.ListCreateAPIView):
    queryset = GPUMetrics.objects.all()
    serializer_class = GPUMetricSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

