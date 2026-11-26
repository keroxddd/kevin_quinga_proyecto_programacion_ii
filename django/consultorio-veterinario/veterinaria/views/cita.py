from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from veterinaria.forms.cita import CitaForm
from .cuenta import perfil_usuario
@login_required
def nueva_cita(request):
    propietario = perfil_usuario(request.user)
    form = CitaForm(request.POST or None, propietario=propietario)
    if request.method == "POST" and form.is_valid():
        form.save(); messages.success(request, "Tu cita fue registrada."); return redirect("panel")
    return render(request, "veterinaria/formulario.html", {"form":form, "titulo":"Agendar una cita"})
