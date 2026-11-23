# 🐾 CONSULTORIO VETERINARIO

## 📌 Descripción del proyecto

El proyecto **Consultorio Veterinario** corresponde a la materia **Programación II**. Tiene como finalidad desarrollar un sistema web que permita administrar y controlar las actividades de un consultorio veterinario, facilitando la gestión de pacientes, propietarios, veterinarios, citas médicas e historiales clínicos.

El sistema se desarrollará utilizando Python, Django, MySQL, HTML y CSS, aplicando una estructura organizada de carpetas y archivos para facilitar su mantenimiento y crecimiento.

## 🎯 Objetivo general

Desarrollar un sistema web para la administración de un consultorio veterinario mediante herramientas de programación que permitan organizar la información y mejorar el control de los servicios veterinarios.

## 🎯 Objetivos específicos

- Registrar y administrar los pacientes (mascotas).
- Gestionar la información de los propietarios.
- Registrar y controlar los veterinarios.
- Administrar las citas y consultas médicas.
- Mantener historiales clínicos de cada mascota.
- Organizar la información mediante una base de datos MySQL.
- Implementar una interfaz web sencilla y organizada.

## 🛠️ Tecnologías utilizadas

| Tecnología | Descripción |
|---|---|
| Python | Lenguaje principal de programación. |
| Django | Framework para desarrollar el sistema web. |
| MySQL | Sistema de gestión de base de datos relacional. |
| HTML | Estructura de las páginas web. |
| CSS | Diseño y presentación visual del sistema. |
| Git | Control de versiones del proyecto. |
| GitHub | Almacenamiento y colaboración del código fuente. |

## 📁 Estructura del proyecto

El proyecto tendrá una organización modular para separar la lógica de programación, la aplicación web, las pruebas y la documentación.

```text
consultorio_veterinario/
│
├── .venv/                         # Entorno virtual de Python
│
├── .gitignore                     # Archivos excluidos de Git
├── README.md                      # Documentación del proyecto
├── requirements.txt               # Dependencias de Python
│
├── python/                        # Código Python independiente
│   ├── main.py                    # Archivo principal
│   └── models.py                  # Modelos o clases de apoyo
│
├── django_app/                    # Aplicación desarrollada en Django
│   │
│   ├── manage.py                  # Administrador del proyecto Django
│   │
│   ├── consultorio/               # Configuración principal de Django
│   │   ├── __init__.py
│   │   ├── settings.py            # Configuración general
│   │   ├── urls.py                # Rutas principales
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── veterinaria/               # Aplicación principal
│   │   ├── __init__.py
│   │   ├── admin.py               # Administración
│   │   ├── apps.py                # Configuración de la aplicación
│   │   ├── models.py              # Modelos de datos
│   │   ├── views.py               # Lógica y vistas
│   │   ├── urls.py                # Rutas de la aplicación
│   │   ├── tests.py               # Pruebas
│   │   └── migrations/            # Migraciones de la base de datos
│   │
│   ├── templates/                 # Plantillas HTML
│   │
│   └── static/                    # Archivos CSS y recursos estáticos
│
├── tests/                         # Pruebas generales
├── docs/                          # Documentación adicional
├── scripts/                       # Scripts de utilidad
└── data/                          # Archivos de datos de apoyo
```

**Importante:** La carpeta `.venv` se encuentra en la raíz del proyecto para que todas las aplicaciones y módulos puedan utilizar el mismo entorno virtual.

## 🐍 Módulo Python

La carpeta `python/` contiene archivos desarrollados en Python para practicar y organizar la lógica independiente del proyecto.

- `main.py`: archivo principal para ejecutar código Python.
- `models.py`: contiene clases y estructuras de datos de apoyo.

## 🌐 Aplicación Django

La carpeta `django_app/` contiene el sistema web desarrollado con Django.

Dentro de esta carpeta se encuentran:

- `consultorio/`: configuración principal del proyecto.
- `veterinaria/`: aplicación encargada de administrar las funcionalidades del consultorio.
- `templates/`: páginas HTML.
- `static/`: archivos CSS y recursos visuales.
- `manage.py`: herramienta para ejecutar comandos de Django.

## 🐶 Funcionalidades principales

### 1. Gestión de pacientes
- Registrar mascotas.
- Consultar información de los pacientes.
- Editar datos de las mascotas.
- Mantener información organizada.

### 2. Gestión de propietarios
- Registrar propietarios.
- Almacenar información de contacto.
- Relacionar propietarios con sus mascotas.

### 3. Gestión de veterinarios
- Registrar veterinarios.
- Consultar información profesional.
- Administrar sus datos.

### 4. Gestión de citas médicas
- Registrar citas.
- Consultar fechas y horarios.
- Asociar citas con mascotas y veterinarios.

### 5. Historial clínico
- Registrar consultas médicas.
- Guardar diagnósticos.
- Consultar antecedentes médicos.

### 6. Vacunas y tratamientos
- Registrar vacunas aplicadas.
- Controlar tratamientos.
- Mantener un seguimiento de la atención veterinaria.

## ⚙️ Instalación y configuración

Los siguientes pasos están orientados a sistemas operativos Linux (Ubuntu).

### 1. Actualizar el sistema

```bash
sudo apt update
sudo apt upgrade -y
```

### 2. Instalar Python y herramientas necesarias

```bash
sudo apt install python3 python3-pip python3-venv git -y
```

Verificar las versiones instaladas:

```bash
python3 --version
pip3 --version
git --version
```

### 3. Instalar MySQL

```bash
sudo apt install mysql-server -y
```

Verificar el servicio:

```bash
sudo systemctl status mysql
```

Si el servicio no está iniciado:

```bash
sudo systemctl start mysql
```

### 4. Crear la carpeta principal del proyecto

```bash
mkdir consultorio_veterinario
cd consultorio_veterinario
```

### 5. Crear el entorno virtual en la raíz

El entorno virtual se creará dentro de la primera carpeta del proyecto con el nombre `.venv`.

```bash
python3 -m venv .venv
```

Activar el entorno virtual:

```bash
source .venv/bin/activate
```

Al activarlo, la terminal mostrará algo parecido a:

```bash
(.venv) usuario@equipo:~/consultorio_veterinario$
```

Actualizar pip:

```bash
python -m pip install --upgrade pip
```

### 6. Instalar Django y el conector de MySQL

Primero, instalar las dependencias necesarias para compilar el conector en Ubuntu:

```bash
sudo apt install python3-dev default-libmysqlclient-dev build-essential pkg-config -y
```

Después, con el entorno virtual activado:

```bash
pip install django mysqlclient
```

Verificar la instalación de Django:

```bash
django-admin --version
```

Guardar las dependencias:

```bash
pip freeze > requirements.txt
```

### 7. Crear el proyecto Django

Desde la carpeta principal, con el entorno virtual activado:

```bash
mkdir django_app
cd django_app
```

Crear el proyecto Django:

```bash
django-admin startproject consultorio .
```

Crear la aplicación principal:

```bash
python manage.py startapp veterinaria
```

Crear las carpetas para las plantillas y archivos estáticos:

```bash
mkdir templates
mkdir static
```

## 🗄️ Configuración de la base de datos MySQL

### 1. Ingresar a MySQL

```bash
sudo mysql
```

### 2. Crear la base de datos y el usuario

Ejecutar las siguientes instrucciones SQL:

```sql
CREATE DATABASE consultorio_veterinario
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

CREATE USER 'veterinaria_user'@'localhost'
IDENTIFIED BY 'cambia_esta_clave';

GRANT ALL PRIVILEGES ON consultorio_veterinario.*
TO 'veterinaria_user'@'localhost';

FLUSH PRIVILEGES;
EXIT;
```

**Nota:** Se debe reemplazar `cambia_esta_clave` por una contraseña propia y segura.

### 3. Configurar Django

Abrir el archivo:

```text
django_app/consultorio/settings.py
```

Buscar la variable `DATABASES` y reemplazar su configuración por:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'consultorio_veterinario',
        'USER': 'veterinaria_user',
        'PASSWORD': 'cambia_esta_clave',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
```

También agregar la aplicación `veterinaria` dentro de `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'veterinaria',
]
```

**Importante:** Las credenciales de MySQL son datos privados. No se deben publicar contraseñas reales en GitHub.

## ▶️ Ejecución del proyecto

Antes de ejecutar Django, ingresar a la carpeta principal del proyecto y activar el entorno virtual:

```bash
cd consultorio_veterinario
source .venv/bin/activate
```

Ingresar a la carpeta de Django:

```bash
cd django_app
```

Aplicar las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

Iniciar el servidor:

```bash
python manage.py runserver
```

Abrir el navegador y acceder a:

```text
http://127.0.0.1:8000/
```

## 👨‍💻 Crear un superusuario

Para acceder al panel de administración de Django:

```bash
python manage.py createsuperuser
```

Ingresar el nombre de usuario, correo electrónico y contraseña solicitados.

Después, acceder a:

```text
http://127.0.0.1:8000/admin/
```

## 🔄 Activar y desactivar el entorno virtual

Activar:

```bash
source .venv/bin/activate
```

Desactivar:

```bash
deactivate
```

## 📦 Instalar las dependencias del proyecto

Si se descarga el proyecto desde GitHub en otro equipo, se debe activar el entorno virtual e instalar las dependencias guardadas:

```bash
pip install -r requirements.txt
```

## 🌿 Control de versiones con Git y GitHub

Inicializar Git desde la carpeta principal:

```bash
git init
```

Agregar los archivos:

```bash
git add .
```

Crear el primer commit:

```bash
git commit -m "Primer commit del proyecto Consultorio Veterinario"
```

Conectar el repositorio remoto:

```bash
git remote add origin https://github.com/keroxddd/kevin_quinga_proyecto_programacion_ii.git
```

Cambiar el nombre de la rama principal a `main`:

```bash
git branch -M main
```

Subir el proyecto:

```bash
git push -u origin main
```

**Nota:** Reemplazar `URL_DEL_REPOSITORIO` por la dirección real del repositorio creado en GitHub.

## 🚫 Archivo .gitignore

El archivo `.gitignore` permite excluir archivos que no deben subirse al repositorio.

Contenido recomendado:

```gitignore
# Entorno virtual
.venv/
venv/

# Archivos Python
__pycache__/
*.py[cod]

# Variables de entorno
.env

# Archivos del sistema
.DS_Store
Thumbs.db

# Configuración de editores
.vscode/
.idea/

# Archivos temporales
*.log
*.tmp

# Archivos de base de datos locales
*.sqlite3
```

## 📚 Etapas de desarrollo

| Etapa | Actividad |
|---|---|
| 1 | Organización de carpetas y estructura del proyecto. |
| 2 | Configuración de Python y entorno virtual. |
| 3 | Instalación y configuración de Django. |
| 4 | Configuración de la base de datos MySQL. |
| 5 | Desarrollo de modelos y funcionalidades. |
| 6 | Creación de interfaces con HTML y CSS. |
| 7 | Pruebas y corrección de errores. |
| 8 | Publicación y control de versiones con GitHub. |

## 🎓 Información académica

**Materia:** Programación II

**Proyecto:** Consultorio Veterinario

**Estudiante:** Kevin Quinga

**Área:** Desarrollo de aplicaciones web

## 📌 Estado del proyecto

En desarrollo.

## 📄 Licencia

Proyecto académico desarrollado con fines educativos para la materia Programación II.
