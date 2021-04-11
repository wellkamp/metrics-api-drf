from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from personalmetrics import views

urlpatterns = [
    path('', views.PCList.as_view()),
    path('<int:pk>/', views.PCDetail.as_view()),
    path('<int:pk>/gpu-metrics/', views.ListGPUMetrics.as_view()),
    path('<int:pk>/memory-metrics/', views.ListGPUMetrics.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)