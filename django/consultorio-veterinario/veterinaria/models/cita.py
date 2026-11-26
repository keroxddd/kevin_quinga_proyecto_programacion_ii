from django.db import models
from .mascota import Mascota
from .veterinario import Veterinario

class Cita(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.PROTECT)
    fecha = models.DateTimeField()
    motivo = models.TextField()
    def __str__(self): return f"{self.mascota} - {self.fecha:%d/%m/%Y %H:%M}"
