from django.urls import path
from personalmetrics.views import PCGPUMetricsList, GPUMetricViewSet

urlpatterns = [
    path('personal-computer/<int:pk>', GPUMetricViewSet.as_view(), name='gpu'),
]