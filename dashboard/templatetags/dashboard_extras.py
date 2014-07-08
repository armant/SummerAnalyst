from django import template

register = template.Library()

@register.filter
def access_dict_value(value, arg):
    return value[arg]