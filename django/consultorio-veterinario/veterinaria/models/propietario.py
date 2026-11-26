from django.db import models
from django.conf import settings

class Propietario(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="perfil_veterinaria")
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=25)
    correo = models.EmailField(blank=True)
    def __str__(self): return self.nombre
