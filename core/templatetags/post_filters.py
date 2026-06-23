from django import template


register = template.Library()


@register.filter(name='titulo_mayusculas')
def titulo_mayusculas(value):
    """Convierte el titulo del post a mayusculas."""
    return str(value).upper()
