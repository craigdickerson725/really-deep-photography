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

@register.filter(name='cloudinary_optimized')
def cloudinary_optimized(image_url, params="w=400&h=300&c=fill&q=auto"):
    """
    Appends Cloudinary transformation parameters to the image URL.
    Default params resize to 400x300 and optimize quality automatically.
    You can override the params by passing a different string.
    """
    if image_url:
        return f"{image_url}?{params}"
    return image_url
