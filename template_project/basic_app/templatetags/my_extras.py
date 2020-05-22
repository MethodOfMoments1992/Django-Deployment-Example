from django import template

register = template.Library()


# Custom template
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg, '') # what we're looking for, what we replace with


# Registering the filter:
#register.filter('cut', cut) # (filter name, filter function)
