from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from personalmetrics.views import PCViewSet, ListGPUMetrics, ListMemoryMetrics

router = routers.DefaultRouter()
# router.register('personal-computer', PCViewSet, basename='PC')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('auth.urls')),
    path('personal-computer/', include('personalmetrics.urls')),
    # path('personal-computer/<int:pk>/gpu-metrics/', ListGPUMetrics.as_view()),
    # path('personal-computer/<int:pk>/memory-metrics/', ListMemoryMetrics.as_view())
]
