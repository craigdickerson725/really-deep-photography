from django.views.generic import ListView
from .models import FAQ

# FAQ list view
class FAQView(ListView):
    model = FAQ
    template_name = 'faq/faq.html'
    context_object_name = 'faqs'

    def get_queryset(self):
        # Show only active FAQs
        return FAQ.objects.filter(is_active=True)
