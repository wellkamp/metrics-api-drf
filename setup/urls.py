from django.contrib import admin
from django.urls import path, include
from metrics import views
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gpu-metrics/', views.GPUMetricsList.as_view()),
]
