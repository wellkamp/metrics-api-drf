from django.contrib import admin

from .models import GPUMetrics


@admin.register(GPUMetrics)
class GPUMetricsAdmin(admin.ModelAdmin):
    list_display = ('id', 'gpu_core',)
