# Workshop Django

Proyecto final integrador desarrollado con Django. La aplicacion permite trabajar con publicaciones, productos, formularios, usuarios, permisos y un panel de administracion personalizado.

## Funcionalidades principales

- Herencia de templates con `core/base.html`, bloques reutilizables, includes y partials.
- CRUD completo de publicaciones con Class Based Views.
- Formularios con validaciones propias mediante Django Forms y ModelForms.
- Busqueda dinamica de productos con metodo GET y filtros ORM `icontains`.
- Registro, login, logout y perfil de usuario.
- Control de acceso con permisos de Django.
- Admin personalizado con `ModelAdmin`, filtros, busqueda, edicion rapida, inlines y acciones.
- Context processors, template tags, filtros e inclusion tags reutilizables.
- Pruebas automatizadas para formularios, busquedas y vistas protegidas.
- Configuracion preparada para despliegue con variables de entorno, WhiteNoise y Gunicorn.

## Requisitos

- Python 3.12 o superior recomendado.
- pip.
- Git.

## Instalacion y configuracion

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

Para desarrollo local se puede mantener `DJANGO_DEBUG=True`. Para produccion, configurar una clave segura en `DJANGO_SECRET_KEY` y usar `DJANGO_DEBUG=False`.

## Migraciones y datos de ejemplo

Aplicar migraciones:

```powershell
python manage.py migrate
```

Cargar datos de ejemplo:

```powershell
python manage.py seed_demo
```

Crear superusuario para ingresar al admin:

```powershell
python manage.py createsuperuser
```

## Ejecutar el proyecto

```powershell
python manage.py runserver
```

URLs utiles:

- Home: `http://127.0.0.1:8000/home/`
- Publicaciones: `http://127.0.0.1:8000/posts/`
- Productos: `http://127.0.0.1:8000/products/`
- Contacto: `http://127.0.0.1:8000/contacto/`
- Registro: `http://127.0.0.1:8000/registro/`
- Login: `http://127.0.0.1:8000/accounts/login/`
- Perfil: `http://127.0.0.1:8000/perfil/`
- Vista protegida de usuarios: `http://127.0.0.1:8000/usuarios/lista/`
- Admin: `http://127.0.0.1:8000/admin/`

## Como probar funcionalidades

1. Ingresar a `/registro/` y crear un usuario.
2. Iniciar sesion desde `/accounts/login/`.
3. Acceder al perfil desde `/perfil/`.
4. Listar publicaciones desde `/posts/`.
5. Crear una publicacion desde `/post/nuevo/`.
6. Editar o eliminar publicaciones desde los botones del listado.
7. Probar busquedas en `/products/` usando nombre o categoria.
8. Ingresar a `/admin/` con un superusuario para gestionar modelos.

## Pruebas automatizadas

Ejecutar:

```powershell
python manage.py test
```

Las pruebas cubren:

- Validacion de `ContactoForm`.
- Validacion de `ProductForm`.
- Busqueda de productos por nombre y categoria.
- Control de acceso a vistas protegidas por permisos.

Tambien se puede verificar la configuracion general con:

```powershell
python manage.py check
```

## Admin personalizado

Modelos principales registrados:

- `Product`: columnas, filtros, busqueda, edicion rapida y accion `activar_productos`.
- `MenuItem`: menu dinamico con acciones para activar/desactivar.
- `Author` y `Libro`: edicion relacionada con `TabularInline`.
- `Post`, `Tag` y `SummaryCard`.

La accion `activar_productos` valida permisos con `request.user.has_perm('core.change_product')`, evita reactivar productos ya activos, muestra mensajes con `message_user` y registra auditoria mediante logging.

## Despliegue

El proyecto esta preparado para despliegue en servicios como Render o PythonAnywhere.

Configuraciones incluidas:

- Variables de entorno con `.env` y `python-dotenv`.
- `DJANGO_SECRET_KEY`, `DJANGO_DEBUG` y `DJANGO_ALLOWED_HOSTS`.
- `STATIC_ROOT` para `collectstatic`.
- WhiteNoise para servir archivos estaticos.
- Gunicorn como servidor WSGI.
- `build.sh` para automatizar instalacion, migraciones y archivos estaticos.

Comandos relevantes para despliegue:

```bash
bash build.sh
gunicorn workshop.wsgi:application
```

En Render, configurar:

- Build Command: `bash build.sh`
- Start Command: `gunicorn workshop.wsgi:application`

## Repositorio

https://github.com/andresdelc21/workshop

## Estado del proyecto

El proyecto cumple con los requisitos principales de la entrega final: templates reutilizables, formularios, busquedas dinamicas, admin personalizado, usuarios, permisos, pruebas y preparacion para despliegue.
