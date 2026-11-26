from django.urls import path
from veterinaria.views import directorio as d
urlpatterns=[path('directorio/veterinarios/',d.veterinarios,name='veterinarios'),path('directorio/veterinarios/<int:pk>/',d.veterinario,name='veterinario'),path('directorio/propietarios/',d.propietarios,name='propietarios'),path('directorio/propietarios/<int:pk>/',d.propietario,name='propietario'),path('directorio/especialidades/',d.especialidades,name='especialidades'),path('directorio/especialidades/<int:pk>/',d.especialidad,name='especialidad')]
