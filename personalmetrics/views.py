from django.http import Http404
from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from .models import PersonalComputer, GPUMetrics, MemoryMetrics
from .serializers import PersonalComputerSerializer, GPUMetricSerializer, MemoryMetricSerializer, \
    ListPersonalComputerSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MyPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 10000


class PCList(APIView):
    """CBV Listando pcs"""
    def get(self, request, format=None):
        queryset = PersonalComputer.objects.all()
        serializer = ListPersonalComputerSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ListPersonalComputerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PCDetail(APIView):
    """CBV Detalhamento de um PC"""
    def get_object(self, pk):
        try:
            return PersonalComputer.objects.get(pk=pk)
        except PersonalComputer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PersonalComputerSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PersonalComputerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListGPUMetrics(generics.ListAPIView):
    """Listando temperaturas da GPU"""
    def get_queryset(self):
        queryset = GPUMetrics.objects.filter(pc_id=self.kwargs['pk']).order_by('-id')[:10]
        return queryset
    serializer_class = GPUMetricSerializer
    # permission_classes = [IsAuthenticated]


class ListMemoryMetrics(generics.ListAPIView):
    """Listando temperaturas da memória RAM"""
    def get_queryset(self):
        queryset = MemoryMetrics.objects.filter(pc_id=self.kwargs['pk']).order_by('-id')[:10]
        return queryset
    serializer_class = MemoryMetricSerializer
    # permission_classes = [IsAuthenticated]


'''
class PCViewSet(viewsets.ModelViewSet):
    queryset = PersonalComputer.objects.all().order_by('id')
    serializer_class = PersonalComputerSerializer
    pagination_class = MyPagination
    http_method_names = ['get', 'put', 'post']
    # permission_classes = [IsAuthenticated]
'''
