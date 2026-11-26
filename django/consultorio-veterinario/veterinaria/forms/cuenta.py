from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from veterinaria.models import Propietario
class RegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=120)
    telefono = forms.CharField(max_length=25)
    email = forms.EmailField(label="Correo electrónico")
    class Meta:
        model = User
        fields = ["username", "nombre", "telefono", "email", "password1", "password2"]
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ["nombre", "telefono", "correo"]
