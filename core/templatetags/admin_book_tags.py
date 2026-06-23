from django import template


register = template.Library()


@register.inclusion_tag('admin/libro_summary.html')
def libro_summary(libro):
    return {
        'libro': libro,
    }
