from django import template
from django.urls import NoReverseMatch, reverse
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag(takes_context=True)
def render_nav_menu(context):
    nav_sections = context.get('nav_sections', [])
    request = context.get('request')
    menu_html = '<ul class="nav-menu">'

    for section in nav_sections:
        name = conditional_escape(section.get('name', 'Sin nombre'))
        url_name = section.get('url_name')

        try:
            url = reverse(url_name)
        except NoReverseMatch:
            url = '#'

        active_class = ''
        if request and request.path == url:
            active_class = ' active'

        menu_html += (
            f'<li class="nav-item{active_class}">'
            f'<a href="{conditional_escape(url)}">{name}</a>'
            '</li>'
        )

    menu_html += '</ul>'
    return mark_safe(menu_html)
