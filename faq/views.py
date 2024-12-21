from django.views.generic import ListView
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from .models import FAQ

# FAQ list view
class FAQView(ListView):
    model = FAQ
    template_name = 'faq/faq.html'
    context_object_name = 'faqs'

    def get_queryset(self):
        # Show only active FAQs
        return FAQ.objects.filter(is_active=True)
