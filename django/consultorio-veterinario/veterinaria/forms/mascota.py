from django import forms
from veterinaria.models import Mascota
class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ["nombre", "especie", "raza", "fecha_nacimiento"]
        widgets = {"fecha_nacimiento": forms.DateInput(attrs={"type":"date"})}
