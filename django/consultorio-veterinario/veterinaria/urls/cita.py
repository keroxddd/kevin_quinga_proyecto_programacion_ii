from django.urls import path
from veterinaria.views import cita
urlpatterns = [path("citas/nueva/", cita.nueva_cita, name="cita_nueva")]
