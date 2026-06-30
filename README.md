# Workshop Django

Proyecto final integrador desarrollado con Django. La aplicación permite trabajar con publicaciones, productos, formularios, usuarios, permisos y un panel de administración personalizado.

## Descripción del proyecto

Workshop Django es una aplicación web pensada como práctica integradora del curso. Su objetivo es reunir en un mismo proyecto los conceptos principales de Django: herencia de templates, formularios, búsquedas dinámicas, autenticación, permisos, administración personalizada, pruebas automatizadas y preparación para despliegue.

El proyecto está orientado a usuarios registrados y administradores. Los usuarios pueden acceder a páginas principales, autenticarse y consultar funcionalidades del sitio. El administrador puede gestionar publicaciones, productos, autores, libros, etiquetas, tarjetas resumen, usuarios y grupos desde el panel de administración.

## Funcionalidades principales

- Herencia de templates con `core/base.html`, bloques reutilizables, includes y partials.
- CRUD completo de publicaciones con Class Based Views.
- Formularios con validaciones propias mediante Django Forms y ModelForms.
- Búsqueda dinámica de productos con método GET y filtros ORM `icontains`.
- Registro, login, logout y perfil de usuario.
- Control de acceso con permisos de Django.
- Admin personalizado con `ModelAdmin`, filtros, búsqueda, edición rápida, inlines y acciones.
- Context processors, template tags, filtros e inclusion tags reutilizables.
- Pruebas automatizadas para formularios, búsquedas y vistas protegidas.
- Configuración preparada para despliegue con variables de entorno, WhiteNoise y Gunicorn.

## Requisitos

- Python 3.12 o superior.
- pip.
- Git.

## Instalación y configuración

Clonar el repositorio:

```powershell
git clone https://github.com/andresdelc21/workshop.git
cd workshop
```

Crear y activar un entorno virtual:

```powershell
python -m venv venv
venv\Scripts\activate
```

Instalar dependencias:

```powershell
pip install -r requirements.txt
```

Crear el archivo de variables de entorno:

```powershell
copy .env.example .env
```

Para desarrollo local se puede mantener `DJANGO_DEBUG=True`. Para producción, configurar una clave segura en `DJANGO_SECRET_KEY`, usar `DJANGO_DEBUG=False` y completar `DJANGO_ALLOWED_HOSTS` con el dominio correspondiente.

## Migraciones y datos de ejemplo

Aplicar migraciones:

```powershell
python manage.py migrate
```

Cargar datos de ejemplo:

```powershell
python manage.py seed_demo
```

Crear un superusuario para ingresar al admin:

```powershell
python manage.py createsuperuser
```

## Ejecutar el proyecto

```powershell
python manage.py runserver
```

URLs útiles en desarrollo:

- Home: `http://127.0.0.1:8000/home/`
- Publicaciones: `http://127.0.0.1:8000/posts/`
- Crear publicación: `http://127.0.0.1:8000/post/nuevo/`
- Productos: `http://127.0.0.1:8000/products/`
- Contacto: `http://127.0.0.1:8000/contacto/`
- Registro: `http://127.0.0.1:8000/registro/`
- Login: `http://127.0.0.1:8000/accounts/login/`
- Perfil: `http://127.0.0.1:8000/perfil/`
- Vista protegida de usuarios: `http://127.0.0.1:8000/usuarios/lista/`
- Admin: `http://127.0.0.1:8000/admin/`

## Cómo probar funcionalidades

1. Ingresar a `/registro/` y crear un usuario.
2. Iniciar sesión desde `/accounts/login/`.
3. Acceder al perfil desde `/perfil/`.
4. Listar publicaciones desde `/posts/`.
5. Crear una publicación desde `/post/nuevo/`.
6. Ver, editar o eliminar publicaciones desde los botones del CRUD.
7. Probar búsquedas en `/products/` usando nombre o categoría.
8. Ingresar a `/admin/` con un superusuario para gestionar modelos.
9. Revisar grupos y permisos desde el admin de Django.

## Pruebas automatizadas

Ejecutar:

```powershell
python manage.py test
```

Las pruebas cubren:

- Validación de `ContactoForm`.
- Validación de `ProductForm`.
- Búsqueda de productos por nombre y categoría.
- Control de acceso a vistas protegidas por permisos.

También se puede verificar la configuración general con:

```powershell
python manage.py check
```

## Admin personalizado

Modelos principales registrados:

- `Product`: columnas, filtros, búsqueda, edición rápida y acción `activar_productos`.
- `MenuItem`: menú dinámico con acciones para activar/desactivar.
- `Author` y `Libro`: edición relacionada con `TabularInline`.
- `Post`, `Tag` y `SummaryCard`.

La acción `activar_productos` valida permisos con `request.user.has_perm('core.change_product')`, evita reactivar productos ya activos, muestra mensajes con `message_user` y registra auditoría mediante logging.

## Despliegue

El proyecto se encuentra preparado para despliegue en servicios como Render o PythonAnywhere.

Configuraciones incluidas:

- Variables de entorno con `.env` y `python-dotenv`.
- `DJANGO_SECRET_KEY`, `DJANGO_DEBUG` y `DJANGO_ALLOWED_HOSTS`.
- `STATIC_ROOT` para `collectstatic`.
- WhiteNoise para servir archivos estáticos.
- Gunicorn como servidor WSGI.
- `build.sh` para automatizar instalación, migraciones y archivos estáticos.

Comandos relevantes para despliegue:

```bash
bash build.sh
gunicorn workshop.wsgi:application
```

Configuración sugerida en Render:

- Build Command: `bash build.sh`
- Start Command: `gunicorn workshop.wsgi:application`

Variables de entorno recomendadas para producción:

- `DJANGO_SECRET_KEY`: clave secreta segura.
- `DJANGO_DEBUG`: `False`.
- `DJANGO_ALLOWED_HOSTS`: dominio público del servicio.
- `DJANGO_SECURE_SSL_REDIRECT`: `True` si el hosting usa HTTPS.
- `DJANGO_SESSION_COOKIE_SECURE`: `True` en producción HTTPS.
- `DJANGO_CSRF_COOKIE_SECURE`: `True` en producción HTTPS.

## Repositorio

https://github.com/andresdelc21/workshop

## Estado del proyecto

El proyecto cumple con los requisitos principales de la entrega final: templates reutilizables, formularios, búsquedas dinámicas, admin personalizado, usuarios, permisos, pruebas automatizadas y preparación para despliegue.
