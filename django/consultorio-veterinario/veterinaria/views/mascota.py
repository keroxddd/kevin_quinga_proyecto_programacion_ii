from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from veterinaria.models import Mascota
from veterinaria.forms.mascota import MascotaForm
from .cuenta import perfil_usuario
@login_required
def guardar_mascota(request, pk=None):
    propietario = perfil_usuario(request.user)
    mascota = get_object_or_404(Mascota, pk=pk, propietario=propietario) if pk else None
    form = MascotaForm(request.POST or None, instance=mascota)
    if request.method == "POST" and form.is_valid():
        registro = form.save(commit=False); registro.propietario = propietario; registro.save()
        messages.success(request, "Mascota guardada."); return redirect("panel")
    return render(request, "veterinaria/formulario.html", {"form":form, "titulo":"Datos de la mascota"})
