from django.contrib import admin
from .models import Propietario, Mascota, Veterinario, Cita, Consulta

admin.site.register([Propietario, Mascota, Veterinario, Cita, Consulta])
