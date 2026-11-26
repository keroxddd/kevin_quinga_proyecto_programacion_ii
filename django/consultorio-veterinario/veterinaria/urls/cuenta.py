from django.urls import path
from veterinaria.views import auth_views as auth
from veterinaria.views import cuenta
urlpatterns = [path("", cuenta.inicio, name="inicio"), path("registro/", cuenta.registro, name="registro"), path("ingresar/", auth.ingresar, name="login"), path("salir/", auth.salir, name="logout"), path("panel/", cuenta.panel, name="panel"), path("perfil/", cuenta.perfil, name="perfil")]
