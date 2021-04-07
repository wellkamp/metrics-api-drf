from django.db import models


class PersonalComputer(models.Model):
    mainboard = models.CharField(max_length=50, null=False)
    gpu = models.CharField(max_length=50, null=False)
    processador = models.CharField(max_length=50, null=False)
    memory = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mainboard

    class Meta:
        verbose_name = 'personal_computer'
        verbose_name_plural = 'personal_computers'