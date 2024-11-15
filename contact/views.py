from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import ContactMessage


# Contact view
class ContactView(TemplateView):
    """Handle the contact form submission."""
    template_name = 'contact/contact.html'

    def post(self, request, *args, **kwargs):
        # Save the message to the database
        ContactMessage.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message'],
        )
        # Display a success message
        messages.success(request, 'Thank you for reaching out! Your message has been sent.')  # noqa
        return redirect('contact')
