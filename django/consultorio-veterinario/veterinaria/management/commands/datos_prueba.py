from datetime import timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from veterinaria.models import Propietario, Mascota, Veterinario, Cita, Consulta, Especialidad
class Command(BaseCommand):
    help='Crea grupos y datos ficticios para desarrollo local.'
    def handle(self,*args,**kwargs):
        clientes,_=Group.objects.get_or_create(name='Clientes')
        consultores,_=Group.objects.get_or_create(name='consultores')
        consultores.permissions.set(Permission.objects.filter(content_type__app_label='veterinaria',codename__in=['view_consulta', 'view_veterinario', 'view_especialidad']))
        for name,group in [('cliente_demo',clientes),('consultor_demo',consultores)]:
            u,created=User.objects.get_or_create(username=name,defaults={'is_staff':False})
            if created: u.set_password('DemoLocal2026!');u.save()
            u.groups.add(group)
        cliente=User.objects.get(username='cliente_demo')
        for i in range(1,6):
            prop,_=Propietario.objects.get_or_create(nombre=f'Persona ejemplo {i}',defaults={'telefono':'0990000000','correo':f'ejemplo{i}@example.com','usuario':cliente if i==1 else None})
            mascota,_=Mascota.objects.get_or_create(propietario=prop,nombre=f'Mascota {i}',defaults={'especie':'Perro'})
            vet,_=Veterinario.objects.get_or_create(nombre=f'Veterinario {i}')
            esp,_=Especialidad.objects.get_or_create(nombre=f'Especialidad {i}');vet.especialidades.add(esp)
            cita,_=Cita.objects.get_or_create(mascota=mascota,motivo='Control de ejemplo',defaults={'veterinario':vet,'fecha':timezone.now()+timedelta(days=i),'creado_por':cliente if i==1 else None})
            Consulta.objects.get_or_create(cita=cita,defaults={'diagnostico':'Control de ejemplo'})
        self.stdout.write(self.style.SUCCESS('Datos ficticios cargados; consulta README para las cuentas iniciales.'))
