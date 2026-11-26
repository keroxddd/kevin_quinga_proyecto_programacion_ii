from django.urls import path
from veterinaria.views import mascota
urlpatterns = [path("mascotas/nueva/", mascota.guardar_mascota, name="mascota_nueva"), path("mascotas/<int:pk>/editar/", mascota.guardar_mascota, name="mascota_editar")]
