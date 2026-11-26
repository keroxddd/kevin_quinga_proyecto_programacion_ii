from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

def ingresar(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        destino=request.POST.get('next', '')
        if destino and url_has_allowed_host_and_scheme(destino, allowed_hosts={request.get_host()}, require_https=request.is_secure()): return redirect(destino)
        return redirect('panel')
    return render(request, 'veterinaria/login.html', {'form':form, 'next':request.GET.get('next', '')})
@require_POST
def salir(request):
    logout(request)
    return redirect('inicio')
