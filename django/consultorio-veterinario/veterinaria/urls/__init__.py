from .cuenta import urlpatterns as cuenta
from .mascota import urlpatterns as mascota
from .cita import urlpatterns as cita
urlpatterns = cuenta + mascota + cita
