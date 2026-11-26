from django.urls import path
from veterinaria.views import cita
urlpatterns=[path('citas/',cita.lista,name='cita_lista'),path('citas/nueva/',cita.guardar,name='cita_nueva'),path('citas/<int:pk>/',cita.detalle,name='cita_detalle'),path('citas/<int:pk>/editar/',cita.guardar,name='cita_editar'),path('citas/<int:pk>/eliminar/',cita.eliminar,name='cita_eliminar')]
