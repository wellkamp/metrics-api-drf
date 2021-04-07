from django.db import models
from pc.models import PersonalComputer

# Create your models here.


class GPUMetrics(models.Model):
    pc = models.ForeignKey(
        PersonalComputer,
        on_delete=models.CASCADE,
        related_name='gpu_temps'
    )
    gpu_core = models.CharField(max_length=50, null=False)
    gpu_memory = models.CharField(max_length=50, null=False)
    gpu_vrm_core = models.CharField(max_length=50, null=False)
    gpu_hot_spot = models.CharField(max_length=50, null=False)
    created_at = models.DateField()
    hour_at = models.TimeField()

    def __str__(self):
        return self.gpu_core

    class Meta:
        verbose_name = 'gpu_metric'
        verbose_name_plural = 'gpu_metrics'


class MemoryMetrics(models.Model):
    pc = models.ForeignKey(
        PersonalComputer,
        on_delete=models.CASCADE,
        related_name='memory_temps'
    )
    used = models.CharField(max_length=50, null=False)
    available = models.CharField(max_length=50, null=False)
    created_at = models.DateField()
    hour_at = models.TimeField()

    class Meta:
        verbose_name = 'memory_metric'
        verbose_name_plural = 'memory_metrics'