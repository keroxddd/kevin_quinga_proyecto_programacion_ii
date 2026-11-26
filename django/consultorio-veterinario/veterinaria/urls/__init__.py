from .cuenta import urlpatterns as cuenta
from .mascota import urlpatterns as mascota
from .cita import urlpatterns as cita
from .consulta import urlpatterns as consulta
urlpatterns = cuenta + mascota + cita + consulta
from .directorio import urlpatterns as directorio
urlpatterns += directorio
