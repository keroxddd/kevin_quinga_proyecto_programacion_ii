# Inicio rápido
Esta es una base inicial; usa SQLite como la configuración existente. No modifica el repositorio remoto.

```bash
cd django/consultorio-veterinario
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requeriments.txt
python manage.py makemigrations veterinaria
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Abre http://127.0.0.1:8000/ y usa Administración para registrar datos. Revisa la versión de Python compatible con las dependencias existentes. Este punto de partida no incluye CRUD público, vacunas ni autenticación propia; el panel administrativo sí permite gestionar los modelos.
