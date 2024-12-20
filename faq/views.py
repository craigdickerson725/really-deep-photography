from django.shortcuts import render
from .models import FAQ

# FAQ list view
def faq_list(request):
    faqs = FAQ.objects.filter(is_active=True)  # Show only active FAQs
    return render(request, 'faq/faq.html', {'faqs': faqs})
