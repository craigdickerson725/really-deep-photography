from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter
def currency(value):
    """Format the value as a currency string."""
    try:
        # Convert the value to a float if it's a SafeString or other non-numeric type
        value = float(value)
        return format_html("${:,.2f}", value)
    except (ValueError, TypeError):
        # If conversion fails, return an empty string
        return ""

@register.filter
def multiply(value, arg):
    """Multiply the value by the arg."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0  # Return 0 if there's an error in conversion
