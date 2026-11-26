from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render
from veterinaria.models import Veterinario, Propietario, Especialidad

def lista_modelo(request, modelo, titulo):
    return render(request,'veterinaria/directorio.html',{'objetos':modelo.objects.all(),'titulo':titulo})
def detalle_modelo(request, modelo, pk):
    return render(request,'veterinaria/directorio_detalle.html',{'objeto':get_object_or_404(modelo,pk=pk)})
@login_required
@permission_required('veterinaria.view_veterinario',raise_exception=True)
def veterinarios(request): return lista_modelo(request,Veterinario,'Veterinarios')
@login_required
@permission_required('veterinaria.view_veterinario',raise_exception=True)
def veterinario(request,pk): return detalle_modelo(request,Veterinario,pk)
@login_required
@permission_required('veterinaria.view_propietario',raise_exception=True)
def propietarios(request): return lista_modelo(request,Propietario,'Propietarios')
@login_required
@permission_required('veterinaria.view_propietario',raise_exception=True)
def propietario(request,pk): return detalle_modelo(request,Propietario,pk)
@login_required
@permission_required('veterinaria.view_especialidad',raise_exception=True)
def especialidades(request): return lista_modelo(request,Especialidad,'Especialidades')
@login_required
@permission_required('veterinaria.view_especialidad',raise_exception=True)
def especialidad(request,pk): return detalle_modelo(request,Especialidad,pk)
