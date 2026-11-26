from django.db import models
from .mascota import Mascota
from .veterinario import Veterinario

class Cita(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT, related_name="citas")
    veterinario = models.ForeignKey(Veterinario, on_delete=models.PROTECT, related_name="citas")
    fecha = models.DateTimeField()
    motivo = models.TextField()
    creado_por = models.ForeignKey("auth.User", null=True, blank=True, on_delete=models.SET_NULL, related_name="citas_creadas")
    class Meta:
        ordering = ["fecha"]
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("cita_detalle", args=[self.pk])
    def __str__(self): return f"{self.mascota} - {self.fecha:%d/%m/%Y %H:%M}"
