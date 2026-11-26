from django.urls import path
from veterinaria.views import consulta
urlpatterns=[path('consultas/',consulta.lista,name='consulta_lista'),path('consultas/<int:pk>/',consulta.detalle,name='consulta_detalle')]
