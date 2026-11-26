from django.db import models

class Veterinario(models.Model):
    especialidades = models.ManyToManyField("veterinaria.Especialidad", blank=True, related_name="veterinarios")
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=25, blank=True)
    class Meta:
        ordering = ["nombre"]
    def __str__(self): return self.nombre
