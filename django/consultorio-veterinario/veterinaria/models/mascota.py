from django.db import models
from .propietario import Propietario

class Mascota(models.Model):
    class Especie(models.TextChoices):
        PERRO = "Perro", "Perro"
        GATO = "Gato", "Gato"
        AVE = "Ave", "Ave"
        OTRO = "Otro", "Otro"
    propietario = models.ForeignKey(Propietario, on_delete=models.PROTECT, related_name='mascotas')
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=60, choices=Especie.choices)
    raza = models.CharField(max_length=60, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    class Meta:
        ordering = ["nombre"]
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("mascota_detalle", args=[self.pk])
    def __str__(self): return self.nombre
