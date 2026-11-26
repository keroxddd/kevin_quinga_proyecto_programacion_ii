from django.urls import path
from django.contrib.auth import views as auth
from veterinaria.views import cuenta
urlpatterns = [path("", cuenta.inicio, name="inicio"), path("registro/", cuenta.registro, name="registro"), path("ingresar/", auth.LoginView.as_view(template_name="veterinaria/login.html"), name="login"), path("salir/", auth.LogoutView.as_view(), name="logout"), path("panel/", cuenta.panel, name="panel"), path("perfil/", cuenta.perfil, name="perfil")]
