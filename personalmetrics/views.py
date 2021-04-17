from datetime import timezone, timedelta, datetime, time
from django.db.models import Max, Min, Avg
from django.http import Http404
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import PersonalComputer, GPUMetrics, MemoryMetrics
from .serializers import PersonalComputerSerializer, GPUMetricSerializer, MemoryMetricSerializer, \
    ListPersonalComputerSerializer, MinMaxValueGPUSerializer, MemoryMetricsValuesSerializer
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
    pagination_class = MyPagination
    """CBV Detalhamento de um PC"""
    def get_object(self, pk):
        try:
            return PersonalComputer.objects.get(pk=pk)
        except PersonalComputer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        personal_computer = self.get_object(pk)
        serializer = ListPersonalComputerSerializer(personal_computer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        personal_computer = self.get_object(pk)
        serializer = ListPersonalComputerSerializer(personal_computer, data=request.data)
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
        queryset = GPUMetrics.objects.filter(pc_id=self.kwargs['pk']).order_by('-id')
        return queryset
    serializer_class = GPUMetricSerializer
    # permission_classes = [IsAuthenticated],


class GPUTempLastFiveDays(APIView):
    """Recupera conforme solicitado dias e intervalo de horas da temperatura gpu_core"""
    def get(self, request, pk, temp):
        days = self.manipulate_days(temp)
        hour_lte = self.manipulate_hours_gte(temp)
        hour_gte = self.manipulate_hours_lte(temp)
        gpu_values = self.get_temps_in_data(self.calc_days(days), hour_gte, hour_lte)
        hours = self.get_hours_in_data(self.calc_days(days), hour_gte, hour_lte)
        return Response({'last_gpu_core': gpu_values, 'last_hour': hours})

    def manipulate_days(self, temp):
        """Manipulando a string de dias"""
        if len(temp) < 6:
            return temp[0:1]
        return temp[0:2]

    def manipulate_hours_lte(self, temp):
        """Manipulando a string de horas menor que"""
        if len(temp) < 6:
            return temp[1:3]
        return temp[2:4]

    def manipulate_hours_gte(self, temp):
        """Manipulando a string de horas maior que"""
        if len(temp) < 6:
            return temp[3:5]
        return temp[4:6]

    def get_hours_in_data(self, data, hour_gte, hour_lte):
        """Recupera as horas na data e horario x, y"""
        query = GPUMetrics.objects.all().filter(created_at=data, hour_at__gte=f'{hour_gte}:00:00.000000',
                                                hour_at__lte=f'{hour_lte}:00:00.000000')
        hour = [obj.hour_at for obj in query]
        return hour

    def get_temps_in_data(self, data, hour_gte, hour_lte):
        """Recupera as temperaturas na data e horario x, y"""
        query = GPUMetrics.objects.all().filter(created_at=data, hour_at__gte=f'{hour_gte}:00:00.000000',
                                                hour_at__lte=f'{hour_lte}:00:00.000000')
        temps = [obj.gpu_core for obj in query]
        return temps

    def calc_days(self, days):
        """Calculo dos dias"""
        data = datetime.today() - timedelta(days=int(days))
        data = data.strftime('%Y-%m-%d')
        return data


class GPUMaxMinAvgValues(APIView):
    """Classe que implementa as métricas Max, Min e Média"""
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        values = self.get_last_seven_values()
        return Response({'avg': self.get_avg_rating(), 'min': self.get_min_rating(), 'max': self.get_max_rating(),
                         'last_gpu_core': self.get_temp_gpu_core(values), 'last_hour': self.get_hour_at(values)})

    def get_max_rating(self):
        return GPUMetrics.objects.filter(pc_id=self.kwargs['pk']).aggregate(Max('gpu_core'))['gpu_core__max']

    def get_min_rating(self):
        return GPUMetrics.objects.filter(pc_id=self.kwargs['pk']).aggregate(Min('gpu_core'))['gpu_core__min']

    def get_avg_rating(self):
        avg = GPUMetrics.objects.filter(pc_id=self.kwargs['pk']).aggregate(Avg('gpu_core'))['gpu_core__avg']
        return round(avg, 1)

    def get_last_seven_values(self):
        return GPUMetrics.objects.all().filter(pc_id=self.kwargs['pk']).order_by('-id')[:7]

    @staticmethod
    def get_temp_gpu_core(values):
        return [obj.gpu_core for obj in values]

    @staticmethod
    def get_hour_at(values):
       return [obj.hour_at.strftime("%H:%M:%S") for obj in values]


class MaxGPUValue(generics.ListAPIView):
    serializer_class = MinMaxValueGPUSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retorna o último valor máximo de temperatura, data e hora"""
        max_rating = GPUMetrics.objects.aggregate(Max('gpu_core'))['gpu_core__max']
        return GPUMetrics.objects.filter(gpu_core=max_rating).order_by('-id')[:1]


class MinGPUValue(generics.ListAPIView):
    serializer_class = MinMaxValueGPUSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retorna o último valor minimo de temperatura, data e hora"""
        min_rating = GPUMetrics.objects.aggregate(Min('gpu_core'))['gpu_core__min']
        queryset = GPUMetrics.objects.filter(gpu_core=min_rating).order_by('-id')[:1]
        return queryset


class ListMemoryMetrics(generics.ListAPIView):
    """Listando temperaturas da memória RAM"""
    def get_queryset(self):
        queryset = MemoryMetrics.objects.filter(pc_id=self.kwargs['pk']).order_by('-id')
        return queryset
    serializer_class = MemoryMetricSerializer
    # permission_classes = [IsAuthenticated]


class MemoryMoreThanTwentyPercent(generics.ListAPIView):
    serializer_class = MemoryMetricsValuesSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MemoryMetrics.objects.filter(used__gte=20).order_by('-id')


class MemoryLassThanTwentyPercent(generics.ListAPIView):
    serializer_class = MemoryMetricsValuesSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        max_rating = MemoryMetrics.objects.filter(used__lte=20).order_by('-id')
        print(max_rating)
        return max_rating



'''
class PCViewSet(viewsets.ModelViewSet):
    queryset = PersonalComputer.objects.all().order_by('id')
    serializer_class = PersonalComputerSerializer
    pagination_class = MyPagination
    http_method_names = ['get', 'put', 'post']
    # permission_classes = [IsAuthenticated]
    
'''