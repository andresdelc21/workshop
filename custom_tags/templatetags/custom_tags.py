from django import template


register = template.Library()


@register.filter
def nombre_completo_mayus(user):
    nombre_completo = f'{user.first_name} {user.last_name}'.strip()

    if not nombre_completo:
        nombre_completo = user.username

    return nombre_completo.upper()


@register.simple_tag
def saludo_personalizado(user):
    nombre = user.first_name or user.username
    return f'Bienvenido, {nombre}!'
