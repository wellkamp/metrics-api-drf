from django.db import models

# Create your models here.


class GPUMetrics(models.Model):
    gpu_core = models.CharField(max_length=50, null=False)
    gpu_memory = models.CharField(max_length=50, null=False)
    gpu_vrm_core = models.CharField(max_length=50, null=False)
    gpu_hot_spot = models.CharField(max_length=50, null=False)
    created_at = models.DateField()
    hour_at = models.TimeField()

    def __str__(self):
        return self.gpu_core

    class Meta:
        verbose_name = 'metric'
        verbose_name_plural = 'metrics'