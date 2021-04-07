from django.contrib import admin
from django.urls import path, include
from pc.views import PCViewSet, PCGPUMetricsList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pc', PCViewSet, basename='PC')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('pc/gpu-metrics/<int:pk>/', PCGPUMetricsList.as_view())
]
