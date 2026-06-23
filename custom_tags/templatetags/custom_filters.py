from django import template


register = template.Library()


@register.simple_tag
def saludo(nombre):
    return f'Hola, {nombre}! Bienvenido a la plataforma.'


@register.filter
def formatear_fecha(fecha):
    if not fecha:
        return ''

    return fecha.strftime('%d/%m/%Y')
