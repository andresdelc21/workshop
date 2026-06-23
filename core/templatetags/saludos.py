from datetime import datetime

from django import template


register = template.Library()


@register.simple_tag
def saludo():
    hora = datetime.now().hour

    if 6 <= hora < 12:
        return 'Buenos dias'
    if 12 <= hora < 20:
        return 'Buenas tardes'
    return 'Buenas noches'
