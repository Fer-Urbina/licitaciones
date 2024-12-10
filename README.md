### Licitaciones Web Application

## Descripción
La aplicación Licitaciones Web es una plataforma diseñada para gestionar licitaciones de manera eficiente. Permite a los usuarios registrarse como licitadores o proveedores. Los licitadores pueden crear y gestionar licitaciones, mientras que los proveedores pueden enviar propuestas y participar en las mismas.

## Funcionalidades
## 1. Funcionalidades para Licitadores
* Crear nuevas licitaciones especificando:
  * Título
  * Descripción
  * Fecha límite
* Ver todas las licitaciones creadas.
* Cerrar manualmente las licitaciones abiertas.
* Revisar propuestas recibidas para una licitación.
* Seleccionar una propuesta ganadora una vez que la licitación esté cerrada.
## 2. Funcionalidades para Proveedores
* Consultar licitaciones abiertas.
* Enviar propuestas para licitaciones específicas.
* Revisar propuestas enviadas.
* Recibir notificaciones de propuestas ganadoras.

## Requisitos Previos

# Tecnologías
* Python 3.11+
* Django 5.1.4
* PostgreSQL

# Dependencias
* django
* djangorestframework
* whitenoise
* python-decouple
* psycopg2-binary

Instala todas las dependencias con:

```bash
pip install -r requirements.txt

 Configuración
1. Variables de Entorno
Crea un archivo .env en el directorio raíz y añade las siguientes variables:

SECRET_KEY=tu-clave-secreta
DB_NAME=nombre-de-tu-base-de-datos
DB_USER=usuario-de-base-de-datos
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=5432

2. Configuración del Servidor
Asegúrate de configurar correctamente DEBUG y ALLOWED_HOSTS en settings.py:


DEBUG = False
ALLOWED_HOSTS = ['licitaciones-np08.onrender.com', 'localhost', '127.0.0.1']

 Cómo Usar
1. Ejecución Local

python manage.py runserver

Accede a http://127.0.0.1:8000 para probar la aplicación localmente.

2. Despliegue
La aplicación está desplegada en Render y está disponible en el siguiente enlace: https://licitaciones-np08.onrender.com

 Estructura del Proyecto
 Principales Apps
usuarios: Gestión de autenticación y roles.
gestion_licitaciones: Creación y administración de licitaciones.
propuestas: Gestión de propuestas enviadas por proveedores.

 Directorio Principal

licitaciones/
├── usuarios/
├── gestion_licitaciones/
├── propuestas/
├── templates/
├── static/
└── manage.py

 Colaboradores
Este proyecto fue desarrollado por Fernando como parte de la asignatura Ingeniería de Software II
