from django.db import models
from .cita import Cita

class Consulta(models.Model):
    cita = models.OneToOneField(Cita, on_delete=models.PROTECT)
    diagnostico = models.TextField()
    tratamiento = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    def __str__(self): return f"Consulta: {self.cita}"
