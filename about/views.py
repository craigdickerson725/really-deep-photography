from django.shortcuts import render
from django.views.generic import TemplateView

# About view
class AboutView(TemplateView):
    """Render the about page."""
    template_name = 'about/about.html'
