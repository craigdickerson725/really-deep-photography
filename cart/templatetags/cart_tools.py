from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """Calculate the subtotal for a given price and quantity."""
    return price * quantity


@register.filter(name='multiply')
def multiply(value, arg):
    """Multiply a value by a given argument."""
    try:
        return value * arg
    except (TypeError, ValueError):
        return 0
