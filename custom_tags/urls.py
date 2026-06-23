from django.urls import path

from .views import BuscarUsuariosView, lista_usuarios


app_name = 'custom_tags'

urlpatterns = [
    path('usuarios/buscar/', BuscarUsuariosView.as_view(), name='buscar_usuarios'),
    path('usuarios/lista/', lista_usuarios, name='lista_usuarios'),
]
