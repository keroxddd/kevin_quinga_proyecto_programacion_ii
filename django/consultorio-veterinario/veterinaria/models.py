from django.db import models

class Propietario(models.Model):
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=25)
    correo = models.EmailField(blank=True)
    def __str__(self): return self.nombre

class Mascota(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.PROTECT, related_name='mascotas')
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=60)
    raza = models.CharField(max_length=60, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    def __str__(self): return self.nombre

class Veterinario(models.Model):
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=25, blank=True)
    def __str__(self): return self.nombre

class Cita(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.PROTECT)
    fecha = models.DateTimeField()
    motivo = models.TextField()
    def __str__(self): return f"{self.mascota} - {self.fecha:%d/%m/%Y %H:%M}"

class Consulta(models.Model):
    cita = models.OneToOneField(Cita, on_delete=models.PROTECT)
    diagnostico = models.TextField()
    tratamiento = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    def __str__(self): return f"Consulta: {self.cita}"
