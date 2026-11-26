from django.test import TestCase
from django.contrib.auth.models import User,Group,Permission
from django.utils import timezone
from datetime import timedelta
from .models import Propietario,Mascota,Veterinario,Cita
class AccesoTest(TestCase):
    def setUp(self):
        self.a=User.objects.create_user('uno',password='PruebaSegura987!')
        self.b=User.objects.create_user('dos',password='PruebaSegura987!')
        self.cons=User.objects.create_user('consultor',password='PruebaSegura987!')
        self.g=Group.objects.create(name='consultores')
        self.g.permissions.add(Permission.objects.get(content_type__app_label='veterinaria',codename='view_consulta'))
        self.cons.groups.add(self.g)
        self.pa=Propietario.objects.create(usuario=self.a,nombre='Uno',telefono='123')
        self.pb=Propietario.objects.create(usuario=self.b,nombre='Dos',telefono='123')
        self.ma=Mascota.objects.create(nombre='A',especie='Perro',propietario=self.pa)
        self.mb=Mascota.objects.create(nombre='B',especie='Gato',propietario=self.pb)
        self.v=Veterinario.objects.create(nombre='Vet')
    def test_accesos(self):
        self.assertEqual(self.client.get('/panel/').status_code,302)
        self.client.force_login(self.cons)
        self.assertEqual(self.client.get('/consultas/').status_code,200)
        self.assertEqual(self.client.get('/directorio/propietarios/').status_code,403)
        self.assertEqual(self.client.get('/admin/').status_code,302)
        self.client.post('/salir/')
        self.assertEqual(self.client.get('/panel/').status_code,302)
    def test_propiedad_y_cita(self):
        self.client.force_login(self.a)
        self.assertEqual(self.client.get(f'/mascotas/{self.mb.pk}/').status_code,404)
        data={'mascota':self.mb.pk,'veterinario':self.v.pk,'fecha':(timezone.localtime()+timedelta(days=5)).strftime('%Y-%m-%dT%H:%M'),'motivo':'Chequeo'}
        self.assertEqual(self.client.post('/citas/nueva/',data).status_code,200)
        self.assertEqual(Cita.objects.count(),0)
        data['mascota']=self.ma.pk
        self.assertEqual(self.client.post('/citas/nueva/',data).status_code,302)
        self.assertEqual(Cita.objects.get().creado_por,self.a)
    def test_eliminar_requiere_post(self):
        self.client.force_login(self.a)
        self.assertEqual(self.client.get(f'/mascotas/{self.ma.pk}/eliminar/').status_code,200)
        self.assertTrue(Mascota.objects.filter(pk=self.ma.pk).exists())
        self.assertEqual(self.client.post(f'/mascotas/{self.ma.pk}/eliminar/').status_code,302)
        self.assertFalse(Mascota.objects.filter(pk=self.ma.pk).exists())
    def test_registro_y_login(self):
        r=self.client.post('/registro/',{'username':'nuevo','nombre':'Nuevo','telefono':'123','email':'nuevo@example.com','password1':'Clave-segura-987!','password2':'Clave-segura-987!'})
        self.assertEqual(r.status_code,302)
        self.assertTrue(Propietario.objects.filter(usuario__username='nuevo').exists())
        self.client.post('/salir/')
        self.assertEqual(self.client.post('/ingresar/',{'username':'nuevo','password':'Clave-segura-987!'}).status_code,302)
