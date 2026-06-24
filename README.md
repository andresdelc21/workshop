# Workshop Django

Aplicacion Django integradora para practicar templates reutilizables, busquedas dinamicas, admin personalizado, usuarios, grupos y permisos.

## Funcionalidades principales

- Herencia de templates con `core/base.html`, bloques, includes y partials.
- Context processors para nombre del sitio, navegacion, grupo del usuario y version del admin.
- Template tags, filtros e inclusion tags reutilizables.
- CRUD de publicaciones con class based views.
- Busqueda dinamica de productos con formulario GET y filtros ORM `icontains`.
- Formulario de contacto con validacion `clean_email`.
- Admin personalizado con `list_display`, `list_filter`, `search_fields`, inlines y acciones masivas.
- Grupos y permisos: `Moderadores` y `Editores`.
- Vista protegida de usuarios con permiso `auth.view_user`.
- Registro y perfil de usuario con login/logout de Django.

## Instalacion

```powershell
cd C:\Users\andre\Documents\workshop
python -m venv ..\venv
..\venv\Scripts\activate
pip install -r requirements.txt
```

## Migraciones y datos de ejemplo

```powershell
python manage.py migrate
python manage.py seed_demo
```

Para crear un superusuario:

```powershell
python manage.py createsuperuser
```

## Ejecutar el proyecto

```powershell
python manage.py runserver
```

URLs utiles:

- Inicio: `http://127.0.0.1:8000/home/`
- Productos: `http://127.0.0.1:8000/products/`
- Publicaciones: `http://127.0.0.1:8000/`
- Contacto: `http://127.0.0.1:8000/contacto/`
- Registro: `http://127.0.0.1:8000/registro/`
- Login: `http://127.0.0.1:8000/accounts/login/`
- Perfil: `http://127.0.0.1:8000/perfil/`
- Usuarios protegidos: `http://127.0.0.1:8000/usuarios/lista/`
- Admin: `http://127.0.0.1:8000/admin/`

## Pruebas

```powershell
python manage.py test
```

Las pruebas cubren:

- Validacion de `ContactoForm`.
- `ProductForm`.
- Busqueda de productos por nombre y categoria.
- Control de acceso a la vista protegida de usuarios.

## Admin

Modelos principales registrados:

- `Product`: columnas, filtros, busqueda, edicion rapida y accion `activar_productos`.
- `MenuItem`: menu dinamico con acciones para activar/desactivar.
- `Author` y `Libro`: edicion relacionada con `TabularInline`.
- `Post`, `Tag`, `SummaryCard`.

La accion `activar_productos` valida permisos, evita reactivar productos ya activos, muestra mensajes con `message_user` y registra auditoria por logging.


## Despliegue

El proyecto incluye configuracion basica para despliegue:

- `ALLOWED_HOSTS` permite localhost y dominios temporales de Ngrok.
- `STATIC_ROOT` esta configurado para `collectstatic`.
- `MEDIA_URL` y `MEDIA_ROOT` estan definidos para archivos subidos.

Comando recomendado antes de desplegar:

```powershell
python manage.py collectstatic
```

Para una demostracion rapida se puede exponer el servidor local con Ngrok:

```powershell
python manage.py runserver
ngrok http 8000
```

Luego se comparte la URL publica generada por Ngrok.
