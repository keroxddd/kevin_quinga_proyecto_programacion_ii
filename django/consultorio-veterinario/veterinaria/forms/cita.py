from django import forms
from django.utils import timezone
from veterinaria.models import Cita, Mascota
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ["mascota", "veterinario", "fecha", "motivo"]
        widgets = {"fecha": forms.DateTimeInput(attrs={"type": "datetime-local"})}
    def __init__(self, *args, propietario, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["mascota"].queryset = Mascota.objects.filter(propietario=propietario)
    def clean_fecha(self):
        fecha = self.cleaned_data["fecha"]
        if fecha <= timezone.now():
            raise forms.ValidationError("Selecciona una fecha futura.")
        return fecha
