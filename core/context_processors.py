from .models import MenuItem


def global_context(request):
    site_name = 'Mi Sitio Django'
    menu_items = MenuItem.objects.filter(active=True).order_by('order', 'name')

    return {
        'site_name': site_name,
        'menu_items': menu_items,
    }



def navigation_context(request):
    sections = [
        {'name': 'Inicio', 'url_name': 'core:home'},
        {'name': 'Productos', 'url_name': 'core:products'},
        {'name': 'Contacto', 'url_name': 'core:contacto'},
        {'name': 'Publicaciones', 'url_name': 'core:post_list'},
    ]
    config = {
        'site_name': 'Mi Sitio Django',
        'show_search': True,
    }

    return {
        'nav_sections': sections,
        'site_config': config,
    }



def admin_version(request):
    return {
        'admin_version': 'Django Admin - version operativa 1.0',
    }
