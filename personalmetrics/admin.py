from django.contrib import admin

from .models import PersonalComputer, GPUMetrics, MemoryMetrics


@admin.register(PersonalComputer)
class PersonalComputerAdmin(admin.ModelAdmin):
    list_display = ('id', 'gpu',)


@admin.register(GPUMetrics)
class GPUMetricsAdmin(admin.ModelAdmin):
    list_display = ('id', 'gpu_core',)


@admin.register(MemoryMetrics)
class MemoryMetricsAdmin(admin.ModelAdmin):
    list_display = ('id', )

