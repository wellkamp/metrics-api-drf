from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from personalmetrics import views

urlpatterns = [
    path('', views.PCList.as_view()),
    path('<int:pk>/', views.PCDetail.as_view()),
    path('<int:pk>/gpu-metrics/', views.ListGPUMetrics.as_view()),
    path('<int:pk>/gpu-metrics/min/', views.MinGPUValue.as_view()),
    path('<int:pk>/gpu-metrics/max/', views.MaxGPUValue.as_view()),
    path('<int:pk>/gpu-metrics/values/', views.GPUMaxMinAvgValues.as_view()),
    path('<int:pk>/memory-metrics/', views.ListMemoryMetrics.as_view()),
    path('<int:pk>/gpu-metrics/lastdays/<str:temp>/', views.GPUTempLastFiveDays.as_view()),
    path('<int:pk>/memory-metrics/morethan/', views.MemoryMoreThanTwentyPercent.as_view()),
    path('<int:pk>/memory-metrics/lassthan/', views.MemoryLassThanTwentyPercent.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)