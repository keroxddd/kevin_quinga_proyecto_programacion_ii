from django.db import models
class Especialidad(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'especialidades'
    def __str__(self): return self.nombre
