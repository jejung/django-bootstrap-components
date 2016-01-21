from django import template

register = template.Library()

@register.inclusion_tag('bootstrap/bootstrap_page.html', takes_context=True)
def bootstrap_page(context):
    return context
