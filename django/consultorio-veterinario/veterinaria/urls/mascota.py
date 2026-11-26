from django.urls import path
from veterinaria.views import mascota
urlpatterns=[path('mascotas/',mascota.lista,name='mascota_lista'),path('mascotas/nueva/',mascota.guardar_mascota,name='mascota_nueva'),path('mascotas/<int:pk>/',mascota.detalle,name='mascota_detalle'),path('mascotas/<int:pk>/editar/',mascota.guardar_mascota,name='mascota_editar'),path('mascotas/<int:pk>/eliminar/',mascota.eliminar,name='mascota_eliminar')]
