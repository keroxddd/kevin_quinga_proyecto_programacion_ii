from django.db import models

class Veterinario(models.Model):
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=25, blank=True)
    def __str__(self): return self.nombre
