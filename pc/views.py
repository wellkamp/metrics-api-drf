from rest_framework import viewsets, generics
from .models import PersonalComputer
from .serializer import PersonalComputerSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class PCViewSet(viewsets.ModelViewSet):
    queryset = PersonalComputer.objects.all()
    serializer_class = PersonalComputerSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class PCGPUMetricsList(generics.RetrieveAPIView):
    queryset = PersonalComputer.objects.all()
    serializer_class = PersonalComputerSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

