from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db import transaction
from django.shortcuts import redirect, render
from veterinaria.forms.cuenta import RegistroForm, PerfilForm
from veterinaria.models import Propietario, Cita

def inicio(request):
    return render(request, "veterinaria/inicio.html")

def registro(request):
    form = RegistroForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        with transaction.atomic():
            user = form.save()
            Propietario.objects.create(usuario=user, nombre=form.cleaned_data["nombre"], telefono=form.cleaned_data["telefono"], correo=form.cleaned_data["email"])
            grupo, _ = Group.objects.get_or_create(name="Clientes")
            user.groups.add(grupo)
        login(request, user)
        return redirect("panel")
    return render(request, "veterinaria/formulario.html", {"form":form, "titulo":"Crear cuenta"})

def perfil_usuario(user):
    perfil, _ = Propietario.objects.get_or_create(usuario=user, defaults={"nombre":user.get_full_name() or user.get_username(), "telefono":"", "correo":user.email})
    return perfil

@login_required
def panel(request):
    perfil = perfil_usuario(request.user)
    return render(request, "veterinaria/panel.html", {"perfil":perfil, "mascotas":perfil.mascotas.all(), "citas":Cita.objects.filter(mascota__propietario=perfil).select_related("mascota", "veterinario").order_by("fecha")})

@login_required
def perfil(request):
    perfil = perfil_usuario(request.user)
    form = PerfilForm(request.POST or None, instance=perfil)
    if request.method == "POST" and form.is_valid():
        form.save(); messages.success(request, "Tus datos se guardaron."); return redirect("panel")
    return render(request, "veterinaria/formulario.html", {"form":form, "titulo":"Mis datos"})
