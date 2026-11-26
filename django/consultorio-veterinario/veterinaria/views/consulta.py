from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from veterinaria.models import Consulta
@login_required
@permission_required('veterinaria.view_consulta',raise_exception=True)
def lista(request): return render(request,'veterinaria/consulta_lista.html',{'consultas':Consulta.objects.select_related('cita__mascota')})
@login_required
@permission_required('veterinaria.view_consulta',raise_exception=True)
def detalle(request,pk): return render(request,'veterinaria/consulta_detalle.html',{'consulta':get_object_or_404(Consulta.objects.select_related('cita__mascota'),pk=pk)})
