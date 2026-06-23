from django import template

from core.models import MenuItem, SummaryCard


register = template.Library()


def _valid_url(url):
    return isinstance(url, str) and url.startswith('/')


@register.inclusion_tag('custom_tags/components/menu.html', takes_context=True)
def render_menu(context, items=None):
    if items is None:
        items = MenuItem.objects.filter(active=True).order_by('order', 'name')

    menu_items = [
        item for item in items
        if getattr(item, 'name', None) and _valid_url(getattr(item, 'url', ''))
    ]

    return {
        'menu_items': menu_items,
        'request': context.get('request'),
    }


@register.inclusion_tag('custom_tags/components/summary_card.html')
def summary_card(title, description, url):
    if not title:
        title = 'Sin titulo'
    if not description:
        description = 'Sin descripcion disponible.'
    if not _valid_url(url):
        url = '/'

    return {
        'title': title,
        'description': description,
        'url': url,
    }


@register.inclusion_tag('custom_tags/components/summary_cards.html')
def summary_cards(cards=None):
    if cards is None:
        cards = SummaryCard.objects.filter(active=True).order_by('order', 'title')

    valid_cards = [
        card for card in cards
        if getattr(card, 'title', None) and _valid_url(getattr(card, 'url', ''))
    ]

    return {
        'cards': valid_cards,
    }


@register.inclusion_tag('custom_tags/components/alert_box.html')
def alert_box(message, alert_type='info'):
    valid_types = {'info', 'warning', 'error'}

    if alert_type not in valid_types:
        alert_type = 'info'
    if not message:
        message = 'Mensaje no disponible.'

    return {
        'message': message,
        'alert_type': alert_type,
    }
