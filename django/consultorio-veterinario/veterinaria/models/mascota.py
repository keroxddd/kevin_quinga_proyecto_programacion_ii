from django.db import models
from .propietario import Propietario

class Mascota(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.PROTECT, related_name='mascotas')
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=60)
    raza = models.CharField(max_length=60, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    def __str__(self): return self.nombre
