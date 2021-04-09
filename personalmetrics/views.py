from rest_framework import viewsets, generics
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import PersonalComputer, GPUMetrics, MemoryMetrics
from .serializers import PersonalComputerSerializer, GPUMetricSerializer, MemoryMetricSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 10000


class PCViewSet(viewsets.ModelViewSet):
    queryset = PersonalComputer.objects.all().order_by('id')
    serializer_class = PersonalComputerSerializer
    pagination_class = MyPagination
    http_method_names = ['get', 'put', 'post']
    # permission_classes = [IsAuthenticated]


class ListGPUMetrics(generics.ListAPIView):
    """Listando temperaturas"""
    def get_queryset(self):
        queryset = GPUMetrics.objects.filter(pc_id=self.kwargs['pk']).order_by('-id')[:10]
        return queryset
    serializer_class = GPUMetricSerializer
    # permission_classes = [IsAuthenticated]


class ListMemoryMetrics(generics.ListAPIView):
    """Listando temperaturas"""
    def get_queryset(self):
        queryset = MemoryMetrics.objects.filter(pc_id=self.kwargs['pk']).order_by('-id')[:10]
        return queryset
    serializer_class = MemoryMetricSerializer
    # permission_classes = [IsAuthenticated]
