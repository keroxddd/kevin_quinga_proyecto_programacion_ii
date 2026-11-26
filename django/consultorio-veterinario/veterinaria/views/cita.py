from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from veterinaria.forms.cita import CitaForm
from veterinaria.models import Cita
from .cuenta import perfil_usuario

def mis_citas(request): return Cita.objects.filter(mascota__propietario=perfil_usuario(request.user)).select_related('mascota','veterinario')
@login_required
def lista(request): return render(request,'veterinaria/lista.html',{'titulo':'Mis citas','objetos':mis_citas(request),'tipo':'cita'})
@login_required
def detalle(request,pk): return render(request,'veterinaria/detalle.html',{'objeto':get_object_or_404(mis_citas(request),pk=pk),'tipo':'cita'})
@login_required
def guardar(request,pk=None):
    propietario=perfil_usuario(request.user)
    obj=get_object_or_404(mis_citas(request),pk=pk) if pk else None
    form=CitaForm(request.POST or None,instance=obj,propietario=propietario)
    if request.method=='POST' and form.is_valid():
        cita=form.save(commit=False)
        if not cita.pk: cita.creado_por=request.user
        cita.save(); messages.success(request,'Cita guardada.'); return redirect('cita_detalle',pk=cita.pk)
    return render(request,'veterinaria/formulario.html',{'form':form,'titulo':'Datos de la cita'})
@login_required
def eliminar(request,pk):
    obj=get_object_or_404(mis_citas(request),pk=pk)
    if request.method=='POST':
        try: obj.delete(); messages.success(request,'Cita eliminada.')
        except ProtectedError: messages.error(request,'No se puede eliminar: esta cita tiene una consulta asociada.')
        return redirect('cita_lista')
    return render(request,'veterinaria/confirmar.html',{'objeto':obj})
