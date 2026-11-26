from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from veterinaria.models import Mascota
from veterinaria.forms.mascota import MascotaForm
from .cuenta import perfil_usuario

def mis_mascotas(request): return Mascota.objects.filter(propietario=perfil_usuario(request.user))
@login_required
def lista(request): return render(request, 'veterinaria/lista.html', {'titulo':'Mis mascotas', 'objetos':mis_mascotas(request), 'tipo':'mascota'})
@login_required
def detalle(request, pk): return render(request, 'veterinaria/detalle.html', {'objeto':get_object_or_404(mis_mascotas(request),pk=pk), 'tipo':'mascota'})
@login_required
def guardar_mascota(request, pk=None):
    propietario=perfil_usuario(request.user)
    mascota=get_object_or_404(mis_mascotas(request), pk=pk) if pk else None
    form=MascotaForm(request.POST or None,instance=mascota)
    if request.method=='POST' and form.is_valid():
        obj=form.save(commit=False); obj.propietario=propietario; obj.save()
        messages.success(request,'Mascota guardada.'); return redirect('mascota_detalle',pk=obj.pk)
    return render(request,'veterinaria/formulario.html',{'form':form,'titulo':'Datos de la mascota'})
@login_required
def eliminar(request,pk):
    obj=get_object_or_404(mis_mascotas(request),pk=pk)
    if request.method=='POST':
        try: obj.delete(); messages.success(request,'Mascota eliminada.')
        except ProtectedError: messages.error(request,'No se puede eliminar: la mascota tiene citas asociadas.')
        return redirect('mascota_lista')
    return render(request,'veterinaria/confirmar.html',{'objeto':obj})
